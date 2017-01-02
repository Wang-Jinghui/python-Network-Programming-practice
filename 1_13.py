# -*- coding:utf-8 -*-
# 有时候并不需要获取很精确的时间
# 在不适用任何第三方库的情况下，写一个简单的SNTP客户端
# 定义常量NTP_SERVER = '0.uk.pool.ntp.org'是客户端要连接的服务器地址
# 定义常量TIME1970 = 2208988800L,是时间1970年1月1日的Epoch值，是一种时间格式
# 创建UDP套接字，使用sendto（）和recvfrom()发送接收数据
# 客户端发送'\x1b'+47*'\0'到服务器
# 服务区返回的信息打包在一个数组中，使用struct模块取出数组的前11个元素，减去TIME1970
import socket
import struct
import time
NTP_SERVER = '0.uk.pool.ntp.org'
TIME1970 = 2208988800L
def sntp_client():
    # UDP套接字
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    data = '\x1b'+47*'\0'
    client.sendto(data,(NTP_SERVER,123))
    data,address = client.recvfrom(1024)
    if data:
        print 'Response received from %s'%str(address)
    t = struct.unpack('!12I',data)[10]   # 取出数组的前11个元素
    t = t - TIME1970
    print 'Time is :%s'%time.ctime(t)
if __name__ == '__main__':
    sntp_client()
