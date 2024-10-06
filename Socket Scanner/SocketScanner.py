import socket
import threading

# Function to scan a single port
def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)  # Timeout of 1 second for each port
    try:
        result = scanner.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open.")
        scanner.close()
    except Exception as e:
        print(f"Error scanning port {port}: {str(e)}")

# Function to scan a range of ports
def scan_ports(ip, start_port, end_port):
    print(f"Scanning IP: {ip} from port {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        thread.start()

# Main function
if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    scan_ports(target_ip, start_port, end_port)
