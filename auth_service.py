import random
import socket
import os
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5050

# Sets 13% crash chance
CRASH_CHANCE = 0.13


def timestamp():
    return datetime.now().strftime("%H:%M:%S")


def handle_request(message):
    # Expected format: LOGIN <username> <password>
    parts = message.strip().split()

    if len(parts) != 3 or parts[0].upper() != "LOGIN":
        return "ERROR Use: LOGIN <username> <password>"

    # Placeholder prototype that returns a fake token
    username = parts[1]
    return f"TOKEN demo-token-for-{username}"


def main():
    print(f"[{timestamp()}] Authentication service starting on {HOST}:{PORT}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"[{timestamp()}] Waiting for login requests...")

        while True:
            connection, address = server.accept()

            with connection:
                message = connection.recv(1024).decode("utf-8").strip()

                if not message:
                    continue

                print(f"[{timestamp()}] Request from {address[0]}: {message}")

                # Simulates random crash
                if random.random() < CRASH_CHANCE:
                    print(f"[{timestamp()}] Simulated service crash triggered.", flush=True)
                    os._exit(1)

                response = handle_request(message)
                connection.sendall((response + "\n").encode("utf-8"))
                print(f"[{timestamp()}] Sent: {response}")


if __name__ == "__main__":
    main()
