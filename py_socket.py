# !/usr/bin/python
# -*- coding: UTF-8 -*-
#
# import socket               # 导入 socket 模块
#
# s = .socket()         # 创建 socket 对象
# host = socket.gethostname() # 获取本地主机名
# print host                  # DESKTOP-ME6P9CV
# port = 12345                # 设置端口
# s.bind((host, port))        # 绑定端口，将套接字绑定到地址，在AF_INET下,以元组（host,port）的形式表示地址.

# s.listen(5)                 # 等待客户端连接
# while True:
#     c, addr = s.accept()     # 建立客户端连接。
#     print '连接地址：', addr
#     c.send('hello')
#     c.close()                # 关闭连接



import time
import socket               # 导入 socket 模块
import serial

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口号

s.connect(("120.77.250.179", port))
# s.connect(("125.81.167.55", port))
# print s.recv(1024) # 接受TCP套接字的数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。

ser = serial.Serial('COM4', 9600, timeout=0.5)  #/dev/ttyUSB0
if ser.isOpen():
    print("open success")
else:
    print("open failed")

while True:
    serial_data = ser.read_all()
    # print serial_data
    s.send(serial_data)

# for i in range(10):
#     s.send("%s" %(i+1))
#     print  "Num: %s" %i

s.close()

# https://yq.aliyun.com/articles/131567?spm=5176.10695662.1996646101.searchclickresult.1bc42408Bc8OgF
# from socket import *
# def SocketServer():
#     try:
#         Colon = ServerUrl.find(':')
#         IP = ServerUrl[0:Colon]
#         Port = int(ServerUrl[Colon+1:])
#         # 建立socket对象
#         print 'Server start:%s'%ServerUrl
#         sockobj = socket(AF_INET, SOCK_STREAM)
#         sockobj.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)
#         # 绑定IP端口号
#         sockobj.bind((IP, Port))
#         # 监听，允许5个连结
#         sockobj.listen(5)
#         # 直到进程结束时才结束循环
#         while True:
#             # 等待client连结
#             connection, address = sockobj.accept( )
#             print 'Server connected by client:', address
#             while True:
#                 # 读取Client消息包内容
#                 data = connection.recv(1024)
#                 # 如果没有data，跳出循环
#                 if not data: break
#                 # 发送回复至Client
#                 RES='200 OK'
#                 connection.send(RES)
#                 print 'Receive MSG:%s'%data.strip()
#                 print 'Send RES:%s\r\n'%RES
#                 # 关闭Socket
#                 connection.close( )
#     except Exception,ex:
#             print ex
# ServerUrl = "192.168.16.15:9999"
# SocketServer()
