from socket import *

# UDP SERVER

# specify port number that the server will listen to
server_port = 8080

# instantiate the socket with:
# AF_INET = Address Family IPv4
# SOCK_DGRAM = configure to accept datagram which is used by UDP protocol
server_socket = socket(AF_INET, SOCK_DGRAM)

# bind the desired port to the server socket. packets will be routed to this socket when addressed to the assigned server port
server_socket.bind(("", server_port))

print("the server is ready to receive messages...")

while True:
    # save messages to socket to variables
    message, client_address = server_socket.recvfrom(2048)

    modified_message = message.decode().upper()

    server_socket.sendto(modified_message.encode(), client_address)




