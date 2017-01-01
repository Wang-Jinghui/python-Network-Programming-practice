#!/usr/bin/env python
# this program is optimized for pyhton 2.7,it may run on any

import socket
def test_socket_modes():
    # create a tcp socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # change the socket mode :block
    s.setblocking(1)
    
    s.settimeout(0.5)
    
    s.bind(('127.0.0.1',0))
    # get address ,port
    socket_address = s.getsockname()
    print 'trivial server launched on socket:%s'%str(socket_address)
    while(1):
        s.listen(1)
if __name__ == '__main__':
    test_socket_modes()
