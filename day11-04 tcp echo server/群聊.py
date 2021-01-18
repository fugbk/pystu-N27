# encoding = utf-8
__author__ = "Ang Li"


import socket
import threading
import datetime
import logging

FORMAT = "%(asctime)s %(threadName)s %(thread)d: %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)
    def __init__(self, ip="0.0.0.0", port=9000):
        self.addr = (ip, port)
        self._sock = socket.socket()    # 创建一个socket， 私有的对象
        self._sock.bind(self.addr)  # 绑定地址
        self.clients = {}   # 空字典，用来保存所有的 socket

    def start(self):
        """启动程序"""
        self._sock.listen()     # 启动监听
        logging.info("server is listing...")
        """
        这个accept线程，用来创建socket，每接入一个连接创建一个socket，多个recv线程
        """
        threading.Thread(target=self.accept).start()    # 需要启动accept线程，不然会阻塞 no-daemon线程

    def accept(self):
        while True:
            sock, raddr = self._sock.accept()   # 允许接入连接，获得一个本地的socket，和远端的ip:port，元组格式
            self.clients[raddr] = sock
            logging.info("{}:{} client is established".format(*raddr))
            threading.Thread(target=self.recv, args=(sock, raddr)).start()      # 接收数据，防止阻塞也要启动多线程

    def recv(self, sock:socket.socket, raddr):  # 传入这个连接的socket和远端的 ip，port
        """接收数据"""
        while True:
            data = sock.recv(1024)  # 接收数据

            if data == b'':
                break

            # 将收到的数据封装下，在发回去。二进制传输需要解码和编码
            msg = "{:%Y%m%d %H:%M:%S} [{}:{}] - {} {}".format(datetime.datetime.now(), *raddr, "wellcome", data.decode())
            print(msg)

            for c in self.clients.values():
                print(c)
                c.send(msg.encode())

    def stop(self):
        """关闭程序"""
        while True:
            cmd = input('>>> ')
            if cmd == b'' or cmd == "quit":     # 收到空信息或者quit 退出程序
                self._sock.close()      # 关闭这个连接
            print(threading.enumerate())


def main():
    a = WeChat()
    a.start()
    a.stop()


if __name__ == '__main__':
    main()