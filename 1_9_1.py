# !usr/bin/env/ python
# this program is optimized for python 2.7 It may run on any
# modify buffer size
import socke

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    # create a cocket
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # get the size of the cocket's send buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print 'buffsize size :%d'%bufsize
    # 
    sock.setsockopt(socket.SOL_SOCKET,socket.TCP_NODELAY,1)  
    sock.setsockopt(socket.SOL_SOCKET,
                    socket.SO_SNDBUF,
                    SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET,
                    socket.SO_RCVBUF,
                    RECV_BUF_SIZE)
    # new　buffsize
    send_buffsize = sock.getsockopt(socket.SOL_SOCKET,
                                    socket.SO_SNDBUF)
    recv_buffsize = sock.getsockopt(socket.SOL_SOCKET,
                                    socket.SO_RCVBUF)
    print 'new sendBuffSize:%d, new recvBuffSize:%d'%(send_buffsize,recv_buffsize)
modify_buff_size()