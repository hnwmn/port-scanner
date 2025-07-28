import socket
import threading
from queue import Queue
import argparse
import ipaddress

parser = argparse.ArgumentParser()
parser.add_argument("target", nargs='+', help="target IP address(es)")
parser.add_argument("-t", "--threads", type=int, default=100, help="number of threads to use")
parser.add_argument("-p", "--ports", type=str, default="1-1023", help="port range to scan (e.g., 1-65535)")
parser.add_argument("--udp", action="store_true", help="scan UDP ports")
parser.add_argument("-o", "--output", type=str, help="output file to save results")
args = parser.parse_args()

num_threads = args.threads

port_range = args.ports.split('-')
port_list = range(int(port_range[0]), int(port_range[1]) + 1)

def scan_target(target):
    queue = Queue()
    open_ports = []

    def portscan(port):
        try:
            if args.udp:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(1)
                sock.sendto(b"", (target, port))
                sock.recvfrom(1024)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target, port))
            return True # port is open
        except:
            return False

    # fills the queue with ports to scan
    def fill_queue(port_list):
        for port in port_list:
            queue.put(port)

    def get_service(port, protocol):
        try:
            return socket.getservbyport(port, protocol)
        except:
            return "unknown"

    # worker function that each thread executes
    def worker():
        protocol = "udp" if args.udp else "tcp"
        while not queue.empty():
            port = queue.get()
            if portscan(port):
                service = get_service(port,protocol)
                print(f"Port {port} is open! Service: {service}")
                open_ports.append((port, service))

    fill_queue(port_list)

    # create the threads and start them
    thread_list = []

    for t in range(num_threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    # wait for all threads to complete
    for thread in thread_list:
        thread.join()

    print(f"Open ports for {target} are:", open_ports)
    return open_ports

for target in args.target:
    open_ports = scan_target(target)
    if args.output:
        with open(args.output, 'a') as f:
            f.write(f"{target}: {open_ports}")
        print(f"Results are saved to {args.output}")