#check open ports

import subprocess

def check_open_ports():
    open_ports = subprocess.check_output(['netstat', '-an'])
    print("Open Ports:\n", open_ports.decode())

if __name__ == "__main__":
    check_open_ports()