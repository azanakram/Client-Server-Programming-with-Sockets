from socket import *
import sys

# Error handling
if (len(sys.argv) != 3):
    sys.exit("Incorrect number of command line arguments")

n_port = int(sys.argv[1])                                       # Store command-line argument: Fixed port number
req_Code = int(sys.argv[2])                                     # Store command-line argument: Request code
serverSocket = socket(AF_INET, SOCK_STREAM)                     # Create Socket with TCP connection
serverSocket.bind(('', n_port))                                 # Bind socket to fixed port

def reverseSentence(sentence):                                  # Function to reverse the sentence
    return sentence[::-1]

def start():                                                    # Start Server
    serverSocket.listen(1)
    print("The server is listening...")
    while True:
        connection, address = serverSocket.accept()
        client_req_code = int(connection.recv(1024).decode())
        
        if client_req_code == req_Code:                         # Checks if the client sent the correct req_code
            # need to send back a random port where we will listen from next
            rSocket = socket(AF_INET, SOCK_DGRAM)               # Create new socket with UDP connection
            rSocket.bind(('',0))                                # Bind the socket to a random *available* port
            r_port = rSocket.getsockname()[1]                   # Store the random port number
            connection.send(str(r_port).encode())               # Send r_port to Client
            sentence, clientAddress = rSocket.recvfrom(2048)    # Accept the Client connection
            reversedSentence = reverseSentence(sentence.decode())        # Reverse the sentence
            rSocket.sendto(reversedSentence.encode(), clientAddress)         # Send the reversed sentence to the client
        
        else:
            print("Incorrect request code from client. The server will close the TCP connection to that client. Please try again.")
        connection.close()

start()