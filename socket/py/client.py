import socket
import time

Host = "server ip"
Port = "server port"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((Host, Port))
    for i in range(10):
        s.sendall(b"msg")
        data = s.recv(1024)
        if data:
            print("received >>", data.decode("UTF-8"))
        time.sleep(0.5)
    s.shutdown(socket.SHUT_RDWR)
    s.close()