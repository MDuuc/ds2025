from mpi4py import MPI
import os

BUFFER_SIZE = 1024

def send_file(filename):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    print(f"Hello from rank {rank} of {size}")


    if rank == 0:
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            return
        
        print(f"Sending file '{filename}'...")
        with open(filename, "rb") as f:
            while chunk := f.read(BUFFER_SIZE):
                for i in range(1, size):  # Send to all other processes
                    comm.send(chunk, dest=i, tag=0)
            # Notify end of file
            for i in range(1, size):
                comm.send(None, dest=i, tag=0)
        print(f"File '{filename}' sent successfully.")

if __name__ == "__main__":
    send_file("image.png")
