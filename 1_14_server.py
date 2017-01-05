# -*- coding:utf-8 -*-
# 简单的回显服务器
import socket
import argparse    # 在命令行中制定tcp端口
host = 'localhost'
data_payload = 2048
backlog = 5
def echo_server(port):
    # 创建一个TCP套接字
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设定启用重复地址
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 绑定到指定的端口
    server_address = (host,port)
    print 'Starting up echo server on %s port %s'%server_address
    sock.bind(server_address)
    # 监听多个客户端
    sock.listen(backlog)
    while True:
        print 'Waiting to receive message from client'
        client,address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print 'Data:%s'%data
            client.send(data)
            print 'sent %s bytes back to %s'%(data,address)
        client.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port',action='store',dest='port',
                        type=int,required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
    

