
import socket
import time
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5050

INTERVAL = 2
TIMEOUT = 1
MAX_MISSED = 3


def timestamp():
    return datetime.now().strftime("%H:%M:%S")


def main():
    missed = 0
    failed = False

    print(f"[{timestamp()}] Heartbeat monitor started")

    while True:
        try:
            with socket.create_connection((HOST, PORT), timeout=TIMEOUT) as s:
                s.settimeout(TIMEOUT)
                s.sendall(b"PING\n")
                response = s.recv(1024).decode().strip()

                if response == "ACK":
                    print(f"[{timestamp()}] Heartbeat OK")
                    missed = 0
                    failed = False
                else:
                    missed += 1

        except (OSError, TimeoutError):
            missed += 1

        if missed > 0:
            print(f"[{timestamp()}] Missed heartbeat: {missed}/{MAX_MISSED}")

        if missed >= MAX_MISSED and not failed:
            alert = f"[{timestamp()}] ALERT: Authentication service is DOWN!"
            print(alert)

            with open("heartbeat.log", "a") as log:
                log.write(alert + "\n")

            failed = True

        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
