import socket
import threading


def auto_reply(c, a):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("[ip:", a[0], "port:", str(a[1]) + "]", ">>", data.decode("UTF-8"))
        c.sendall(data + b" [auto reply]")
    c.close()
    lis.remove(c)
    print(c, "close")


Host = ""
Port = 6969
lis = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host, Port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        print(addr)
        if conn not in lis:
            lis.append(conn)
            t = threading.Thread(target=auto_reply, args=(conn, addr))
            t.setDaemon(True)
            t.start()