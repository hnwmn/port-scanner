import socket
import threading
from queue import Queue
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("target", help="target IP address")
parser.add_argument("-t", "--threads", type=int, default=100, help="number of threads to use")
parser.add_argument("-p", "--ports", type=str, default="1-1023", help="port range to scan (e.g., 1-65535)")
args = parser.parse_args()

target = args.target
num_threads = args.threads

port_range = args.ports.split('-')
port_list = range(int(port_range[0]), int(port_range[1]) + 1)

queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True # port is open
    except:
        return False

# fills the queue with ports to scan
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

# worker function that each thread executes
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)

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

print("Open ports are:", open_ports)