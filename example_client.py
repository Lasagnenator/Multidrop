import time
from funcs import *
import os

print("Scanning")

scan_results = [0]
run_in_thread(scan2, scan_results)
while scan_results[0]==0:
    time.sleep(1)
    #print(scan_results)

if len(scan_results[0])==0:
    raise BaseException("Could not find a service")
for result in scan_results[0]:
    print(result["host"], result["name"])

requested_host = input("What host to connect to: ")
name, host, port = find_port(requested_host)

client_sock = create_client_socket()
client_sock = connect_client(client_sock, host, port)

file_path = input("Path to file: ")
length = os.stat(file_path).st_size

client_sock.send(os.path.basename(file_path)+"\n"+str(length)+"\n")

allow = client_sock.recv(1)
if allow=="0":
    print("File denied")
    raise BaseException("Denied file")

file = open(file_path, "rb")
sent = 0
data = file.read()

try:
    percent = [0]
    ret = [0]
    run_in_thread(send_data, ret=ret, i=0, client_sock, data, percent)
    while ret[0]==0:
        time.sleep(1)
        print("{}% complete".format(percent[0]*100))
    print("sent all data")
except IOError:
    pass
finally:
    client_sock.close()
print("Disconnected")
input("Closing.")

##try:
##    while True:
##        data = input("Input: ")
##        if len(data)==0:break
##        client_sock.send(data)
##except IOError:
##    pass
##
##client_sock.close()
##print("Disconnected")
