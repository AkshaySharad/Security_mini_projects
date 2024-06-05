#simple port scanner
import socket  # for connecting
import sys
from colorama import init, Fore

# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX


def is_port_open(host, port):
    s = socket.socket()
    try:

        s.connect((host, port))

    except:
        return False
    else:
        return True


host = 'http://scanme.nmap.org/'
host = '192.168.56.1'
# port = 80
for port in range(1, 1025):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
    else:
        print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")


#advanced port scanner

try:
    for port in range(1,5000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))

        if result ==0:
            print("Port {}:        Open".format(port))
            sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:

    print("Hostname could not be resolved. Exiting")

    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()
