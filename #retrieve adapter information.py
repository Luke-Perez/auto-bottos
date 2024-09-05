#retrieve adapter information

import subprocess

def get_network_adapter_info():
    adapter_info = subprocess.check_output(['netsh', 'interface', 'ip', 'show', 'config'])
    print("Network Adapter Information:\n", adapter_info.decode())

if __name__ == "__main__":
    get_network_adapter_info()