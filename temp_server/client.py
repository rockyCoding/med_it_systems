import socket
from time import sleep

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
temp = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(bytearray('temp', 'utf8'))
        data = float(s.recv(1024).decode('utf8'))
        print(str(round(data, 1)) + ' (' + str(round(data-temp, 1)) + ')')
        temp = data
        sleep(2.5)


