
import socket

def start_server(host='127.0.0.1', port=65216, buffer_size=1024):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}")
    
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    filename_length = int(conn.recv(buffer_size).decode())
    filename = conn.recv(filename_length).decode()
    print(f"Receiving file: {filename}")

    # Save the file with its original name
    with open(filename, "wb") as f:
        print("Receiving file data...")
        while True:
            data = conn.recv(buffer_size)
            if not data:  
                break
            f.write(data)
    print(f"File '{filename}' received successfully.")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()

