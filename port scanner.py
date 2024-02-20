import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.05)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
            return True
        else:
            print(f"Port {port} is closed")
            return False
        sock.close()
    except socket.error as err:
        print(f"Error connecting to {ip}:{port} - {err}")
        return False

ip = input("Enter the target IP address: ")

start_port = 0
end_port = 1000

open_ports = []

for port in range(start_port, end_port + 1):
    if scan_port(ip, port):
        open_ports.append(port)

with open("open_ports.txt", "w") as file:
    for port in open_ports:
        file.write(f"Open port on {ip}:Port no {port}\n")

print(f"\nOpen ports on {ip}: {open_ports}")
print("Saved to open_ports.txt")
