import protocol
import socket
USER_IP = "0.0.0.0"
SEND_IP = "147.235.220.168"
def listen(queue):
    #create socket
    listen_socket = socket.socket()
    listen_socket.bind((USER_IP, protocol.PORT))
    listen_socket.listen(1)
    client_socket, addr = listen_socket.accept()
    queue.put("Server is waiting for a connection...")
    #listen to new messeges
    while(True):
        valid_protocol, input = protocol.get_msg(client_socket)
        if valid_protocol:
            queue.put(input) #if input is valid put in queue for print in gui
def send(input):
    #create socket
    send_socket = socket.socket()
    send_socket.connect((SEND_IP, protocol.PORT))

    packet = protocol.create_msg(input)  # create packet
    send_socket.send(packet) #send
    send_socket.close()






