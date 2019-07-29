import socket
import time

Host = "server ip"
Port = "server port"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, Port))
    while 1:
        s.sendall(b"msg")
        data = s.recv(1024)
        if data:
            print("received >>", data.decode("UTF-8"))
        time.sleep(0.5)
    s.close()