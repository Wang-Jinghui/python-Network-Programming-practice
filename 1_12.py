# -*- coding:utf-8 -*-
# 从网络时间服务器会的精确的时间
# Network Time Protocol   
import ntplib
from time import ctime               
def print_time():
    ntp_client = ntplib.NTPClient()                
    response = ntp_client.request('pool.ntp.org')  
    print ctime(response.tx_time)

if __name__ == '__main__':
    print_time()
