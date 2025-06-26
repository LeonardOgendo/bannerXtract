import socket
import sys

def grab_banner(ip: str, port: int, timeout: float = 2.0):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, port))

        try:
            banner = sock.recv(1024).decode(errors="ignore").strip()
            if banner:
                print(f"[+] {ip}:{port} -> {banner}")
            else:
                print(f"[-] {ip}:{port} -> No banner received")
        except socket.timeout:
            print(f"[-] {ip}:{port} -> No response (recv timeout)")
        sock.close()
    
    except socket.timeout:
        print(f"[-] {ip}:{port} -> Connection timed out")

    except ConnectionRefusedError:
        print(f"[-] {ip}:{port} -> Connection refused")

    except Exception as e:
        print(f"[!] {ip}:{port} -> {e}")


def is_valid_ip(ip: str) -> bool:
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def main():
    ip = input("Enter the target IP address: ").strip()

    if not is_valid_ip(ip):
        print("Invalid IP address")
        sys.exit(1)

    try:
        port = int(input("Enter the target port number: ").strip())
        if not (1 <= port <= 65535):
            raise ValueError
    except ValueError:
        print("Invalid port number")
        sys.exit(1)

    grab_banner(ip, port)

if __name__ == "__main__":
    main()