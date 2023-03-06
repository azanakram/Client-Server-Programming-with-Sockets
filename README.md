# Client-Server-Programming-with-Sockets
TCP and UDP socket programming in a client-server environment designed with Python

The client sends a request to the server to reverse a string that is given as command line input.

We use a two-stage communication process, a negotiation stage and a transaction stage.

In the negotiation stage, we make a TCP socket connection through a fixed negotiation port (<n_port>) of the server. Here, the client passes along the request code (<req_code>) which the server validates. If valid, the server replies back with a random available port number (<r_port>) where it will await for the actual client request. If invalid, the server disconnects the client, and continues listening on <n_port> for any future client requests.

In the transaction stage, we make a UDP socket connection to the server in the <r_port> we were given. It is here that the client sends to the server the string, and the server reverses it and sends it back. Once received, the client prints out the reversed string, closes the connection and exits.

## How to run the program
We must first run the server before we run the client. Navigate to the directory where Server.py is located, and execute the following command:
### python Server.py <n_port> <req_code>
where <n_port> is a fixed and available port number, and <req_code> is an integer.

      Example: python Server.py 8080 26

Now we run the client program. Navigate to the directory where the client program is located, and execute the following command:
### python Client.py <server_address> <n_port> <req_code> <str_msg>
where <server_address> can be the Hostname or IP address of where the server program is running, <n_port> is the fixed port number that the server program is listening on, <req_code> is the request code the server is expecting, and <str_msg> is the string message that will be reversed.

      Example: python Client.py localhost 8080 26 'abc def'
      Example Output: fed cba
