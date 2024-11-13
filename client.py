import socket

clientName = "Client of Shyam Venkatesan" # Client name declared
host = "127.0.0.1" # Host set to localhost IP (set to ipconfig server value for classmate test)
port = 5432 # Port set to number > 5000

# Executes until valid input found
while True:
    # Takes in input for integer in range [1, 100]
    clientNum = input("Enter a number between 1 and 100: ")
    # Tries to cast clientNum to an integer
    try:
        clientNum = int(clientNum)
    # Catches value errors and repeats the loop
    except ValueError:
        print("The input must be of integer type.")
        continue
    # Ends loop regardless of whether integer is in range [1, 100] to provide a way to terminate the server
    break

# Client socket is created with IPv4 and TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects to server using host and port 
client.connect((host, port))
print("Client socket requested connection to server socket.")

# Message string with client's name and sum 
messageStr = clientName + ',' + str(clientNum)

# Message is encoded and sent to server
client.send(messageStr.encode('utf-8'))
print("Client sent message to server.")

# Checks for invalid clientNum to know that server will terminate
if(clientNum < 1 or clientNum > 100):
    # Closes client socket early because server won't send a response
    print("Client socket will terminate: invalid client number.")
    client.close()
    exit()

# Recieves up to 1024 bytes from server and decodes it into a string
recieveStr = client.recv(1024).decode('utf-8')
print("Client recieved response from server.")

# Splits the recieved string into server name and number with , as delimiter
serverName, serverNum = recieveStr.split(',')

# Sum of serverNum and clientNum
sum = clientNum + int(serverNum)

# Displays Client's Name and Number, Server's Name and Number, and the Sum
print("Client Name: " + clientName + "," + " Server Name: " + serverName)
print("Server Number: " + serverNum + "," + " Client Number: " + str(clientNum) + "," +  " Sum: " + str(sum))

# Client socket is closed to terminate the program
print("Client socket will terminate.")
client.close()