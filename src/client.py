import socket
from settings import PORT, HOST
# Define the host and port to connect to (server's IP address)

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))
    print("Connected to server at", HOST, "port", PORT)
    # Send data to the server
    s.sendall(b'Hello, server')
    # Receive data from the server
    data = s.recv(1024)

print('Received:', data.decode())