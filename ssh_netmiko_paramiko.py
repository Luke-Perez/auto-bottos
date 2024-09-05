#MUST pip install netmiko paramiko
#Features of This Script:
#Backup Configuration: Connects to a Cisco device, retrieves the running configuration, and saves it to a file.
#Check Device Status: Retrieves and prints the IP interface status of the device.
#Execute Custom Command: Allows you to input and execute any custom command on the device.
#How to Use:
#Install Required Libraries: Ensure you have Netmiko and Paramiko installed.
#Update Device Details: Replace the placeholder values in the device dictionary with your actual device details.
#Run the Script: Execute the script and follow the prompts.
#This script can be extended further to include more devices, schedule tasks, or integrate with other network management tools

import os
import paramiko
from netmiko import ConnectHandler

#Define device details
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
    'secret': 'secret',  # Enable password
}

def backup_config(device):
    try:
        connection = ConnectHandler(**device)
        connection.enable()
        config = connection.send_command('show running-config')
        with open(f"{device['host']}_backup.txt", 'w') as file:
            file.write(config)
        print(f"Configuration backup for {device['host']} completed.")
        connection.disconnect()
    except Exception as e:
        print(f"Failed to backup configuration for {device['host']}: {e}")

def check_device_status(device):
    try:
        connection = ConnectHandler(**device)
        connection.enable()
        status = connection.send_command('show ip interface brief')
        print(f"Device status for {device['host']}:\n{status}")
        connection.disconnect()
    except Exception as e:
        print(f"Failed to check status for {device['host']}: {e}")

def execute_custom_command(device, command):
    try:
        connection = ConnectHandler(**device)
        connection.enable()
        output = connection.send_command(command)
        print(f"Output for command '{command}' on {device['host']}:\n{output}")
        connection.disconnect()
    except Exception as e:
        print(f"Failed to execute command on {device['host']}: {e}")

if __name__ == "__main__":
    backup_config(device)
    check_device_status(device)
    custom_command = input("Enter a custom command to execute: ")
    execute_custom_command(device, custom_command)