
# port-scanner

This script is a multithreaded port scanner written in Python. It uses a default of 100 threads and checks a default range of ports (1-1023), listing any open ports found.

## Usage/Example

```
% python3 port-scanner.py -h         
usage: port-scanner.py [-h] [-t THREADS] [-p PORTS] [--udp] [-o OUTPUT] target [target ...]

positional arguments:
  target                target IP address(es)

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        number of threads to use
  -p PORTS, --ports PORTS
                        port range to scan (e.g., 1-65535)
  --udp                 scan UDP ports
  -o OUTPUT, --output OUTPUT
                        output file to save results
```

```
% python3 port-scanner.py 192.168.1.1

Port 22 is open! Service: ssh
Port 23 is open! Service: telnet
Port 80 is open! Service: http
Port 443 is open! Service: https
Open ports for 192.168.1.1 are: [(22, 'ssh'), (23, 'telnet'), (80, 'http'), (443, 'https')]
```

## Todo

- [x] Scan UDP ports, currently only TCP.

- [x] Include additional output information like the service running on the open port.

- [x] Allow scanning of multiple IP addresses.

- [x] Add an option to save the scan results to a file (e.g. `--output results.txt`).
