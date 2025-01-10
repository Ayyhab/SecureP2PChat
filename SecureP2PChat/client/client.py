import socket

# Server details
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    # Receive peer details
    peer_info = client_socket.recv(1024).decode()
    print(f"Connected to peer: {peer_info}")

    client_socket.close()

if __name__ == "__main__":
    connect_to_server()
