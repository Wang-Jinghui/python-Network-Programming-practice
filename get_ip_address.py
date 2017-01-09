# -*- coding:utf-8 -*-
import socket
# 获取目标主机的ip 地址
def get_remote_machine_info():
    remote_host = 'www.baidu.com'     # 远端主机名
    try:
        print 'IP address:%s'%socket.gethostbyname(remote_host)
    except socket.error ,err_msg:
        print '%s:%s'%(remote_host,err_msg)


# 主机地址格式的转换
from binascii import hexlify
def convert_ip4_address():
    for ip_add in ['127.0.0.1','192.168.0.1']:
        packed_ip_add = socket.inet_aton(ip_add)
        unpacked_ip_add = socket.inet_ntoa(packed_ip_add)
        print packed_ip_add
        print 'ip address:%s => packed:%s,unpacked:%s'%(ip_add,hexlify(packed_ip_add),unpacked_ip_add)

# 通过制定的端口和协议，找到对应的服务
def find_server_name():
    protocolname = 'tcp'     # 协议名字
    for port in  [80,21]:
        # 通过端口获取服务名
        print 'port :%s ,server name :%s'%(port,socket.getservbyport(port,protocolname))
    print 'port :%s ,server name :/%s'%(53,socket.getservbyport(53,'udp'))

# 主机字节序和网路字节序之间的转换
# 把操作系统发出的数据转换为网络字节顺序
def convert_integer():
    data = 1234
    print 'original:%s =>long host type order:%s,Network byte order:%s'%(data,
                                                                         socket.ntohl(data),
                                                                         socket.htonl(data))
    print 'original:%s =>short host order:%s,Nerwork order:%s'%(data,
                                                                socket.ntohs(data),
                                                                socket.htons(data))
# 设定，获取套接字超时时间
def test_socket_timeout():
    # 构造套接字，地址族，套接字类型
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print 'default socket timeout:%s'%s.gettimeout()
    # 设定套接字超时时间
    s.settimeout(100)
    print 'current socket timeout:%s'%s.gettimeout()






