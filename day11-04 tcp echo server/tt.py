# encoding = utf-8
__author__ = "mcabana.com"

import socket


server = socket.socket()    # 创建一个socket对象

ip, port = "0.0.0.0", 9200

server.bind((ip, port))     # tuple ,绑定 ip,port
server.listen()     # 启动监听

s1, addr = server.accept()      # 建立连接, 并创建新socket。这是个元组格式

s1.send(b'hello')   # 通过新创建的socket发送数据
date = s1.recv(1024)    # 接收数据

print(date)

s1.close()  # 关闭新socket

server.close()  # 关闭服务端socket