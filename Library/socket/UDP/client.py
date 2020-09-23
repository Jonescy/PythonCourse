from socket import *
from threading import Thread
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('192.168.101.103', 8882))
addr = ('192.168.101.103', 8881)


def send_data():
    while True:
        data = input(':')
        s.sendto(data.encode(), addr)


def recv_data():
    while True:
        s.recvfrom(1024)


if __name__ == '__main__':

    t1 = Thread(target=send_data)
    t2 = Thread(target=recv_data)
    t1.start()
    t2.start()
