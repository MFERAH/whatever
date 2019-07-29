import socket
import threading


def auto_reply():
    while 1:
        for c, a in lis:
            data = c.recv(1024)
            if not data:
                continue
                lis.remove((c, a))
                c.close()
            print("[ip:", a[0], "port:", str(a[1]) + "]", ">>", data.decode("UTF-8"))
            c.sendall(data + b" [auto reply]")


Host = ""
Port = 6969
lis = []
num = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((Host, Port))
    s.listen(5)
    t = threading.Thread(target=auto_reply)
    t.start()
    while 1:
        pack = s.accept()
        if pack not in lis:
            lis.append(pack)
        print(lis)
