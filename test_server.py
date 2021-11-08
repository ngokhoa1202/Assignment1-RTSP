import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('',4000))
print(type(sock))
while True:
    data, addr = sock.recvfrom(20480)
    print(str(data))
    msg = bytes("Hello I am server").encode('utf-8')
    print(addr)
    sock.sendto(msg, addr)