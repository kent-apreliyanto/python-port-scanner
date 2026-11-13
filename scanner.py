import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

COMMON_SERVICE = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    135: "RCP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL"
}
def scan_port(ip: str, port: int):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            
            result = sock.connect_ex((ip, port))
            if result == 0:
                service_name = COMMON_SERVICE.get(port, "unknown Service")
                print(f"[+] Port {port:<4} is OPEN | Service: {service_name}")
    except Exception:
        pass
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Concurrent Network Port Scanner")
    parser.add_argument("target", help="The target IP address to scan (e.g., 127.0.0.1)")
    args = parser.parse_args()
    
    TARGET_IP = args.target
    
    print(f"--- Starting aggresive network scan on {TARGET_IP} ---")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        for current_port in range(1, 2025):
            executor.submit(scan_port, TARGET_IP, current_port)
            
    print("--- Scan completed ---")
    