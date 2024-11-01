# SOCKET PROGRAMMING EXERCISE

Credits: [Computer Networking: a Top-Down Approach (8th ed.) J.F. Kurose, K.W. Ross, Pearson, 2020](http://gaia.cs.umass.edu/kurose_ross)

I'm learning more about computer networking.  It's an interesting topic and understanding networking concepts comes in handy when hosting web applications since, for example, it's nice to know what the DNS is when you're configuring DNS records.  It's also nice to know what IP addresses and port numbers are for.

The socket programming exercise here is from Chapter 2 of the credited text.

Chapter 2 - The Application Layer dives into a variety of topics:
- Principles of Network Applications
- The Web and HTTP
- Email infrastructure (mail clients, SMTP servers), SMTP, IMAP
- The Domain Name Service: DNS
- Peer-to-Peer File Distribution
- Video Streaming and Content Distribution Networks
- Socket Programming: Creating Network Applications

# UPD SOCKET
**upd client**
```py
from socket import *

# configure client socket to send message to server socket
server_address = ("localhost", 8080)
client_socket = socket(AF_INET, SOCK_DGRAM)

# accept input from user
message = input("input lowercase sentence\n")

# send and receive message from server process
try:
    client_socket.sendto(message.encode(), server_address)
    modified_message, server_address = client_socket.recvfrom(2048)
    print(modified_message.decode())

finally:
# close socket connection
    client_socket.close()
```

**upd server**
```py
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
```


# TCP SOCKET
**tcp client**
```py
from socket import *

server_address = ("localhost", 8080)
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(server_address)

sentence = input("Say hello > ")

try:
    client_socket.send(sentence.encode())
    response = client_socket.recv(1024)
    print("From Server: ", response.decode())

finally:
    client_socket.close()
```

**tcp server**
```py
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
```
