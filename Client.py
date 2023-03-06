from socket import *
import sys

# Error handling
if (len(sys.argv) != 5):
    sys.exit("Incorrect number of command line arguments.")


serverAddr = sys.argv[1]                                        # Store command-line argument: Hostname
n_port = int(sys.argv[2])                                       # Store command-line argument: Fixed port number
req_code = sys.argv[3]                                          # Store command-line argument: Request code
sentence = sys.argv[4]                                          # Store command-line argument: Sentence to be reversed

clientSocket = socket(AF_INET, SOCK_STREAM)                     # Create Socket with TCP connection
clientSocket.connect((serverAddr, n_port))                      # Connect to server with fixed n_port
clientSocket.send(req_code.encode())                            # Send req_code for validation

r_port = clientSocket.recv(1024).decode()                       # Server returns random available port if valid req_code, empty string otherwise

if r_port != '':                                                # If req_code is valid
    rClientSocket = socket(AF_INET, SOCK_DGRAM)                 # Create socket with UDP connection
    rClientSocket.sendto(sentence.encode(), (serverAddr, int(r_port)))      # Send sentence to server
    reversedSentence, serverAddress = rClientSocket.recvfrom(2048)      # Recieve reversed sentence from server

    print(reversedSentence.decode())                            # Print reversed string

clientSocket.close()                                            # Close TCP connection


