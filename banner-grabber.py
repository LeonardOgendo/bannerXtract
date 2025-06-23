import socket

def grab_banner(ip, port, timeout=2):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, port))
        
        banner = sock.recv(1024).decode().strip()
        print(f"[+] {ip}:{port} -> {banner}")

        sock.close()
    except socket.timeout:
        print(f"[-] {ip}:{port} -> No response (Timed out)")
    except Exception as e:
        print(f"[!] Error on {ip}:{port} -> {e}")