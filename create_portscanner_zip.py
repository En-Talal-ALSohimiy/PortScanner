import zipfile

project_files = {
    "PortScanner/scanner.py": '''
import socket

def scan_ports(target, ports):
    print(f"🔍 Scanning target: {target}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is open")
        sock.close()

if __name__ == "__main__":
    target_ip = input("🖥️ Enter target IP address: ")
    ports_to_scan = range(20, 1025)
    scan_ports(target_ip, ports_to_scan)
''',

    "PortScanner/README.md": '''
# 🔎 PortScanner

A lightweight Python-based port scanner to identify open TCP ports on a target IP address.

## 🚀 How to Run

```bash
python scanner.py
