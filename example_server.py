from funcs import *
import time

server_sock = create_server_socket()
server_sock, host_port = advertise(server_sock)

connected_client = [None]
accept_connection(server_sock, connected_client)

print("Listening for connection.")
while connected_client[0]==None:
    time.sleep(1)
print("\nConnected", end="\n")

client_sock, client_info = connected_client[0]
print("Connection from", client_info)
stop_advertising(server_sock)

header = client_sock.recv(1024)
file_name, file_size = header.split("\n")

accept = input("Accept file {} with size {} bytes? (Y/N)".format(file_name, file_size))
if accept.lower().startswith("y"):
    accept = "1"
    client_sock.send(accept)
    print("Accepting file")
else:
    accept = "0"
    client_sock.send(accept)
    print("Denying file")
    #then end
    raise BaseException("Denied file")

data = b""
recv = b"0"

path = input("Path of folder to download to: ")

try:
    while len(recv)!=0:
        recv = client_sock.recv(1024)
        print(recv)
        data += recv
        #update[0] = len(data) #Percentage complete
    name, *others = data.split("\n")
    #if len(data)!=int(length):
        #raise ConnectionError("Data length did not match.")
    with open(path+name, "wb+") as f:
        f.write(others.join("\n"))
except IOError:
    pass
finally:
    server_sock.close()
    client_sock.close()

print("Disconnected")
input("Closing")

##try:
##    while True:
##        data = client_sock.recv(1024)
##        if len(data)==0:break
##        print(data)
##except IOError:
##    pass
##
##print("Disconnected")
##server_sock.close()

