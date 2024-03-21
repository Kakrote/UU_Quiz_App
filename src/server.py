import socket

# Define the host and port to listen on
HOST = 'localhost'  # Listen on all available interfaces
PORT = 65432

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the host and port
    s.bind((HOST, PORT))
    # Listen for incoming connections
    s.listen()
    print("Server listening on", HOST, "port", PORT)
    # Accept a connection
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                break
            print('Received:', data.decode())
            # Send data back to the client
            conn.sendall(b"Hello CLient")