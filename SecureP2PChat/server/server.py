import socket
import logging

# Configure logging
logging.basicConfig(
    filename="logs/server.log", 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Server configuration
HOST = "127.0.0.1"  # Localhost
PORT = 5000         # Port to listen on

def start_server():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)  # Listen for 2 clients

    logging.info(f"Server started on {HOST}:{PORT}")
    print(f"Server started on {HOST}:{PORT}")

    try:
        # Accept first client
        print("Waiting for Client 1...")
        client_socket1, addr1 = server_socket.accept()
        logging.info(f"Client 1 connected: {addr1}")
        print(f"Client 1 connected: {addr1}")

        # Accept second client
        print("Waiting for Client 2...")
        client_socket2, addr2 = server_socket.accept()
        logging.info(f"Client 2 connected: {addr2}")
        print(f"Client 2 connected: {addr2}")

        # Exchange details
        print("Exchanging client details...")
        client_socket1.sendall(f"{addr2[0]}:{addr2[1]}".encode())
        client_socket2.sendall(f"{addr1[0]}:{addr1[1]}".encode())
        logging.info("Client details exchanged successfully.")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print(f"Error occurred: {e}")
    finally:
        # Close connections
        client_socket1.close()
        client_socket2.close()
        server_socket.close()
        logging.info("Server shut down.")
        print("Server shut down.")

if __name__ == "__main__":
    start_server()
