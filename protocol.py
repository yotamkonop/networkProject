LENGTH_FIELD_SIZE = 4
PORT = 8820


def create_msg(data):
    """
    Create a valid protocol message, with length field
    """

    length = str(len(data)).zfill(LENGTH_FIELD_SIZE)
    return (length + data).encode()


def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """
    length = my_socket.recv(LENGTH_FIELD_SIZE).decode()
    if not length.isnumeric():
        return False, "Error"  # Handle client disconnection
    # Read actual message
    data = my_socket.recv(int(length)).decode()

    return True, data