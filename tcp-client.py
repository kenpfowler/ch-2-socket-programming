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