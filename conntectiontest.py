# install the scapy library
# pip insall scapy
#Features of This Script:
#ARP Request: Sends ARP requests to all IP addresses in the specified range.
#Capture Response: Captures the ARP responses to identify active devices.
#Display Results: Prints the IP and MAC addresses of active devices on the VLAN.
#How to Use:
#Install Required Library: Ensure you have scapy installed.
#Run the Script: Execute the script and enter the IP range you want to scan when prompted.
#This script should help you identify active devices on a VLAN by scanning for connectivity

from scapy.all import ARP, Ether, srp

def scan_vlan(ip_range):
    # Create an ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send the packet and capture the response
    result = srp(packet, timeout=2, verbose=False)[0]

    # Parse the response
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

if __name__ == "__main__":
    ip_range = input("Enter the IP range to scan (e.g., 192.168.1.0/24): ")
    devices = scan_vlan(ip_range)
    print("Active devices on the VLAN:")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")