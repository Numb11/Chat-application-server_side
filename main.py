import socket
client = 0
def send_text(sending_socket, text):
  text = text + "\n"
  data = text.encode()
  sending_socket.send(data)  





def get_text(receiving_socket):
    buffer = ""

    socket_open = True
    while socket_open:
        # read any data from the socket
        data = receiving_socket.recv(1024)

        # if no data is returned the socket must be closed
        if not data:
            socket_open = False

        # add the data to the buffer
        buffer = buffer + data.decode()

        # is there a terminator in the buffer
        terminator_pos = buffer.find("\n")
        # if the value is greater than -1, a \n must exist
        while terminator_pos > -1:
            # get the message from the buffer
            message = buffer[:terminator_pos]
            # remove the message from the buffer
            buffer = buffer[terminator_pos + 1:]
            # yield the message (see below)
            yield message
            # is there another terminator in the buffer
            terminator_pos = buffer.find("\n")




def connect():
    global client
    server_socket.listen() #Listening for a connection to be made
    print("Waiting for Connection")
    connection_socket, address = server_socket.accept() #accept connection
    print(f"Client connected with IP: {address}") #type 127.0.0.1:8081 in the url
    message = ("-------------------You have connected!-------------------------")
    send_text(connection_socket, message)
    client = client + 1


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8082))
#get clients any number, wait for message, get ip and message then forward this to the ip included in that message if cant say no client exists.
run = True
connect()
while run:
   message = server_socket.recv(1024)
   message.split(",")
   sendto = message[-1] 
   message = message[0]
   print ("Transmitting",message,"to",sendto)
   server_socket.sendto(message.encode(),(sendto,8081))

