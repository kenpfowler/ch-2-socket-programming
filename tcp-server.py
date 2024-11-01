import socket

# Define server address and port
server_address = ('localhost', 8080)

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {server_address}")


while True:
    # Wait for a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established.")

    # Receive data from the client
    data = client_socket.recv(1024)
    if data:
        print(f"Received data: {data.decode()}")
        # Send a response back to the client
        client_socket.sendall("Hello, Client!".encode())

    # Close the connection with the client
    client_socket.close()
