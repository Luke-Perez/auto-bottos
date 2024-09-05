#trace route to host

import subprocess

def trace_route(host):
    trace = subprocess.check_output(['tracert', host])
    print(f"Trace Route to {host}:\n", trace.decode())

if __name__ == "__main__":
    host_to_trace = input("Enter the host to trace: ")
    trace_route(host_to_trace)