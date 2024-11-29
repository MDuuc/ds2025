import socket
import os

def send_file(filename, host='127.0.0.1', port=65216, buffer_size=1024):
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    # Send the filename length and the filename
    filename_encoded = os.path.basename(filename).encode()
    filename_length = str(len(filename_encoded)).encode()
    client_socket.sendall(filename_length.ljust(buffer_size)) 
    client_socket.sendall(filename_encoded)  

    # Send the file data
    with open(filename, "rb") as f:
        print("Sending file data...")
        while chunk := f.read(buffer_size):
            client_socket.sendall(chunk)
    print(f"File '{filename}' sent successfully.")

    client_socket.close()

if __name__ == "__main__":
    send_file("image.png") 