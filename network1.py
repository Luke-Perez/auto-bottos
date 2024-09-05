import subprocess

def check_network_status():
    status = subprocess.check_output(['netsh', 'interface', 'show', 'interface'])
    print("Network Status:\n", status.decode())

def get_ip_configuration():
    ipconfig = subprocess.check_output(['ipconfig'])
    print("IP Configuration:\n", ipconfig.decode())

def ping_host(host):
    ping = subprocess.check_output(['ping', '-n', '4', host])
    print(f"Ping {host}:\n", ping.decode())

if __name__ == "__main__":
    check_network_status()
    get_ip_configuration()
    host_to_ping = input("Enter the host to ping: ")
    ping_host(host_to_ping)