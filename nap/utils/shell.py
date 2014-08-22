#coding:utf-8
'''
Created on Aug 22, 2014

@author: root
'''
import os
import re

def ping(ip,count=10,timeout=15):
    "ping "
    cmd="/bin/ping %s -c %s -w %s" % (ip,count,timeout)
    return os.popen(cmd).read() 
    

def test_ping(ip,count=10,timeout=15,loss_rate=100):
    "test_ping "
    result = ping(ip,count,timeout) 
    ping_match = re.compile('(\d+)\spackets transmitted, (\d+)\sreceived,\s(\d+(.\d+)?)\%\spacket\sloss,\stime\s(\d+)')
    lost_rate = ping_match.findall(result)
    if ( not lost_rate or int(lost_rate[0][2]) >= loss_rate ):
        return False
    return True


def test1():
    print test_ping("114.114.114.114",5,5)
    print ping("114.114.114.114",5,5)
    

if __name__ == '__main__':
    test1()