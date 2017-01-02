# -*- coding:utf-8 -*-
# 重用套接字地址
import socket

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # get the old state of the SO_REUSEADDR option
    old_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print 'old sock state ：%s'%old_state
    # 修改socket.SO_REUSEASSR 的vlaue
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    new_state = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print 'new sock state：%s'%new_state
    local_port = 8282
    srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
   
    srv.bind(('',local_port))
    srv.listen(1)
    print 'listening on port ：%s'%local_port
    while True:
        try:
            connection,addr = srv.accept()
            print 'connected by %s:%s'%(addr[0],addr[1])
        except KeyboardInterrupt:
            break
        except socket.error,msg:
            print '%s'%(msg,)
if __name__ == '__main__':
    reuse_socket_addr()