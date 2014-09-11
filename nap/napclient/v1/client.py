#coding:utf-8
'''
Created on Aug 25, 2014

@author: demi
'''

from nap.napclient.v1 import net_monitor


class Client(object):
    """Client v1."""
    def __init__(self):
        self.net_monitor = net_monitor.NetMonitorManager(self)
        
        

if __name__ == '__main__':
    pass