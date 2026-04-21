import socket
import time

port_names = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-ALT"
}

target = input("Enter target IP: ")

print(f"\nScanning target: {target}")
print("Please wait...\n")

start_time = time.time()

open_ports = []

ports_to_scan = [21, 22, 80, 443, 3306, 8080]

for port in ports_to_scan:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        open_ports.append(port)

    s.close()

end_time = time.time()

# Output results
print("🔍 Scan Results:\n")

if open_ports:
    for p in open_ports:
        service = port_names.get(p, "Unknown")
        print(f"Port {p} ({service}) is OPEN")
else:
    print("No open ports found.")

print(f"\n⏱ Scan completed in {end_time - start_time:.2f} seconds")