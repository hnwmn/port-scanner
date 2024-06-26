
# port-scanner

This script is a multithreaded port scanner written in Python. It uses a default of 100 threads and checks a default range of ports (1-1023), listing any open ports found.

## Usage/Example

```
% python3 port-scanner.py -h

usage: port-scanner.py [-h] [-t THREADS] [-p PORTS] target

positional arguments:
  target                target IP address

optional arguments:
  -h, --help                        show this help message and exit
  -t THREADS, --threads THREADS     number of threads to use
  -p PORTS, --ports PORTS           port range to scan (e.g., 1-65535)
```

```
% python3 port-scanner.py 192.168.1.1

Port 22 is open!
Port 23 is open!
Port 80 is open!
Port 443 is open!
Open ports are: [22, 23, 80, 443]
```

## Todo

- [ ] Scan UDP ports, currently only TCP.

- [ ] Include additional output information like the service running on the open port.

- [ ] Allow scanning of multiple IP addresses (either from the command line or from a file).

- [ ]  Add subnet scanning (e.g. `192.168.1.0/24`) to identify all live hosts on the subnet and their open ports.

- [ ] Add an option to save the scan results to a file (e.g. `--output results.txt`)
