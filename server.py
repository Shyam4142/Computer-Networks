import socket
import random

serverName = "Server of Shyam Venkatesan" # Server name declared
host = "127.0.0.1" # Host set to localhost IP (set to 0.0.0.0 for classmate test)
port = 5432 # Port set to number > 5000

# Server socket is created with IPv4 and TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds server to the host and port variables
server.bind((host, port))

# Server starts listening for connections with up to 1 backlog
server.listen(1)
print("Server is listening for client connections on port: " + str(port))

# Server continously looks for new clients
while True:
    # When there is a client request, server stores the client socket and address
    client, address = server.accept()
    print("Server accepted connection from client address: " + str(address))

    # Recieves up to 1024 bytes from client and decodes it into a string
    recieveStr = client.recv(1024).decode('utf-8')

    # Splits the recieved string into client name and number with , as delimiter
    clientName, clientNum = recieveStr.split(',')

    print("Client Name: " + clientName + "," + " Server Name: " + serverName)

    # If the client number is not within bounds [1, 100]
    if not(1 <= int(clientNum) <= 100):
        # Client connection is closed and server breaks out of the loop (way to terminate infinite loop)
        print("Server recieved out of range number from client. Server will close sockets and terminate.")
        client.close()
        break

    # The server chooses random integer in [1, 100] range
    serverNum = random.randint(1, 100)

    # Sum of serverNum and clientNum
    sum = serverNum + int(clientNum)
    print("Server Number: " + str(serverNum) + "," + " Client Number: " + clientNum + "," +  " Sum: " + str(sum))

    # Response string with its own server name and sum 
    responseStr = serverName + "," + str(serverNum)
    
    # Response is encoded and sent to the client
    client.send(responseStr.encode('utf-8'))
    print("Server sent response message to client.")

    # Client socket is closed
    client.close()
    print("Server closed connection to the client socket.")
    print("Server is listening for client connections on port: " + str(port))

# Server socket is closed
server.close()