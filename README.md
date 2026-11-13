# Concurrent Network Port Scanner

A fast, multithreaded command-line port scanner built with Python. This tool aggressively scans network ports to identify open doors and common active services.

## Features
- **Concurrent Execution:** Utilizes `ThreadPoolExecutor` to deploy 50 concurrent workers, drastically reducing scan times compared to sequential scanning.
- **Service Identification:** Automatically maps open ports to common network services (e.g., FTP, SSH, HTTP, SMB).
- **CLI Interface:** Built with `argparse` for seamless terminal usage and dynamic IP targeting.
- **Stealthy Connection:** Uses `socket.connect_ex` for silent connection probing without raising fatal application errors.

## Technology Stack
- Python 3
- `socket` (Low-level TCP/IP networking)
- `concurrent.futures` (Multithreading)
- `argparse` (CLI argument parsing)

## How to Run
1. Clone this repository.
2. Run the script via terminal and provide the target IP address:
   ```bash
   python scanner.py 127.0.0.1

## Security Notice
This tool is intended for educational purposes and authorized network auditing only. The author is not responsible for any misuse, damage, or illegal activities caused by this program. Any unauthorized scanning of networks or systems without explicit, written permission from the network owner is strictly prohibited.