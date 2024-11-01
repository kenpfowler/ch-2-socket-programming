from socket import *

# configure client socket to send message to server socket
server_name = "localhost"
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)

# accept input from user
message = input("input lowercase sentence\n")

# send and receive message from server process
try:
    client_socket.sendto(message.encode(), (server_name, server_port))
    modified_message, server_address = client_socket.recvfrom(2048)
    print(modified_message.decode())

finally:
# close socket connection
    client_socket.close()

