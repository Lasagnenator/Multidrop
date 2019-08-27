
from bluetooth import *
import config
from threading import Thread

def scan():
    return discover_devices(duration=2, lookup_names=True, flush_cache=False, lookup_class=False)

def scan2():
    return find_service(uuid=config.UUID)

def find_port(address:str)->["name", "host", "port"]:
    services = find_service(uuid=config.UUID, address=address)
    if len(services)==0:
        raise BaseException("Could not find a service")
    first_match = services[0]
    port = first_match["port"]
    #name = first_match["name"]
    host = first_match["host"]
    name = lookup_name(address)
    return [name, host, port]

def advertise(sock:BluetoothSocket)->[BluetoothSocket, "port"]:
    sock.listen(1)
    advertise_service(sock, config.name,
                      service_id = config.UUID,
                      service_classes = [config.UUID, SERIAL_PORT_CLASS],
                      profiles = [SERIAL_PORT_PROFILE],
                      provider = "Multidrop Systems"
                      )
    port = sock.getsockname()[1]
    return [sock,port]

def send_data(sock:BluetoothSocket, data:b"string", percentage = [0])->BluetoothSocket:
    while sent<length:
        sent += sock.send(data[sent:])
        percentage[0] = sent/length
    return sock

def recieve_data(sock:BluetoothSocket, size:int)->[b"data", BluetoothSocket]:
    data = sock.recv(size)
    return data, sock

def end_connection(sock:BluetoothSocket)->None:
    sock.close()

def create_server_socket()->BluetoothSocket:
    sock = BluetoothSocket(RFCOMM)
    sock.bind(("", PORT_ANY))
    return sock

def create_client_socket()->BluetoothSocket:
    return BluetoothSocket(RFCOMM)

def connect_client(sock, host, port)->"sock":
    sock.connect((host,port))
    return sock

def _accept_connection(sock, ret:list):
    ret[0] = sock.accept()

def accept_connection(sock, ret:list):
    t = Thread(target=_accept_connection, args=(sock, ret))
    t.start()

def run_in_thread(func, ret:list, i=0, *args):
    def temp(func,  ret, i, *args):
        ret[i] = func(*args)
    t = Thread(target=temp, args=(func, ret, i, *args))

def quit(server_sock, client_sock, connected_sock):
    stop_advertising(server_sock)
    server_sock.close()
    client_sock.close()
    connected_sock.close()
