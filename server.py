import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(5)

print('Server is listening on {}:{}'.format(*server_address))

# List to store connected client addresses
pc_connected = []

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(*client_address))
    print('This is the client address:', client_address)
    pc_connected.append(client_address)

    try:
        # Receive data from the client
        data = client_socket.recv(1024)
        print('Received data:', data.decode())
        print('Connected clients:', pc_connected)

        # Select a client to send a message to
        print('Select a client to send a message to:')
        for i, address in enumerate(pc_connected):
            print(i+1, address[1])  # Display only the port number
        client_selection = input('Enter the client port number: ')

        selected_client_address = None
        for address in pc_connected:
            if str(address[1]) == client_selection:
                selected_client_address = address
                break

        if selected_client_address:
            response = input('Message you want to send to the client {}: '.format(selected_client_address[1]))
            client_socket.sendall(response.encode())
        else:
            print('Invalid client selection.')

    finally:
        # Close the connection
        client_socket.close()
