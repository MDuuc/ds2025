from mpi4py import MPI

BUFFER_SIZE = 1024

def receive_file(output_filename):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank != 0:  # Only non-root processes receive
        with open(output_filename, "wb") as f:
            while True:
                chunk = comm.recv(source=0, tag=0)
                if chunk is None:  # End of file
                    break
                f.write(chunk)
        print(f"Process {rank}: File '{output_filename}' received successfully.")

if __name__ == "__main__":
    receive_file(f"received_file_{MPI.COMM_WORLD.Get_rank()}.jpg")
