import socket
import tempGenerator as tg

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

temp = 0
byteRef = bytearray('temp', 'utf8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        counter = 0
        while True:
            data = conn.recv(1024)
            if data== byteRef and counter == 0:
                temp = tg.startTempGenerator()
                conn.sendall(bytearray(str(temp), 'utf8'))
                counter += 1
            elif data== byteRef and counter >= 1:
                temp = tg.tempGenerator(temp)
                conn.sendall(bytearray(str(temp), 'utf8'))
                counter += 1
            else:
                conn.sendall(bytearray('Unknown Request', 'utf8'))