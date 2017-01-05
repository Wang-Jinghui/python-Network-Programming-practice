# -*- coding:utf-8 -*-
import socket
import argparse
host = 'localhost'
def echo_client(port):
    # create a tcp socket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # connect the socket to the server
    server_address = (host,port)
    print ' connect to %s port %s'%(server_address)
    sock.connect(server_address)
    # send data
    try:
        massage = 'hello body,how are you '
        print 'send massage is：%s'%massage
        sock.sendall(massage)
        # look for the response
        amount_received = 0
        amount_expected = len(massage)
        while amount_received < amount_expected:
            data = sock.recv(16)

            amount_received += len(data)
            print 'received:%s'%data
    except socket.error ,e:
        print 'socket error:%s'%str(e)
    except Exception,e:
        print 'other ecception:%s'%str(e)
    finally:
        print 'closing connection to the server'
        sock.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='socket server example')
    parser.add_argument('--port',action='store',dest='port',type=int,
                        required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)

