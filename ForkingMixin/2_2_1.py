# -*- coding:utf-8 -*-
# ForkingMixIn 会为每个客户端请求都派生一个新的进程
# ForkingServer类继承自TCPServer 和 ForkingMixIn类
# ForkingServerRequestHandler 继承自SocketServer库提供的BaseRequestHandler类
import os
import socket
import threading
import SocketServer
SERVER_HOST = 'localhost'
SERVER_PORT = 0    # 告诉内核动态分配端口
BUF_SIZE = 1024
ECHO_MSG = 'Hello echo server'
# 客户端类
class ForkingClient():
    def __init__(self,ip,port):
        # 流式套接字
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((ip,port))

    def run(self):
        # 系统分配的进程ID
        current_process_id = os.getpid()
        print 'pid %s sending the massage to the server:%s'%(current_process_id,ECHO_MSG)
        # 发送数据，返回发送数据长度
        sent_data_length = self.sock.send(ECHO_MSG)
        print 'sent %d characters,so far...'%sent_data_length
        # 接受缓冲区大小的数据
        response = self.sock.recv(BUF_SIZE)
        print 'pid %s received %s'%(current_process_id,response[5:])
    def shutdown(self):
        # 关闭套接字
        self.sock.close()


# 服务器请求处理类
class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # server接受缓冲区大小的数据
        data = self.request.recv(BUF_SIZE)
        # server进程ID
        current_process_id = os.getpid()
        response = '%s: %s'%(current_process_id,data)
        print 'server sending response [current_process_id: data]=[%s]'%response
        # 把接收的数据在发送给客户端
        self.request.send(response)
        return

# 服务器类
class ForkingServer(SocketServer.ForkingMixIn,SocketServer.TCPServer,):
    pass
def main():
    # 创建服务器类 实例
    server = ForkingServer((SERVER_HOST,SERVER_PORT),ForkingServerRequestHandler)
    ip,port = server.server_address
    # 服务器进程
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print 'Server loop running pid: %s'%os.getpid()
    # 创建客户端实例
    client1 = ForkingClient(ip,port)
    # 发送 等待接收数据
    client1.run()
    client2 = ForkingClient(ip,port)
    client2.run()
    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()
if __name__=='__main__':
    main()

