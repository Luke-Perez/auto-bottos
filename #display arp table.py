#display arp table

import subprocess

def display_arp_table():
    arp_table = subprocess.check_output(['arp', '-a'])
    print("ARP Table:\n", arp_table.decode())

if __name__ == "__main__":
    display_arp_table()