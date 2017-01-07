# -*- coding:utf-8 -*-
# 多线程套接字服务器
import os
import socket
import threading
import SocketServer
SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024     # 缓冲区大小

def client(ip,port,massage):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    try:
        sock.sendall(massage)
        response = sock.recv(BUF_SIZE)
        print 'client received %s'%response
    finally:
        sock.close()

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(BUF_SIZE)
        current_thread = threading.current_thread()
        response = '%s:%s'%(current_thread.name,data)
        self.request.sendall(response)
class ThreadTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass
if __name__ == '__main__':
    server = ThreadTCPServer((SERVER_HOST,SERVER_PORT),ThreadedTCPRequestHandler)
    ip,port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print 'Server loop running on thread:%s'%server_thread.name
    client(ip,port,'Hello from client 1')
    client(ip,port,' Hello form client 2')
    client(ip,port,'  Hello from client 3')
    server.shutdown()


