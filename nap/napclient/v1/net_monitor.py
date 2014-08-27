#coding:utf-8
'''
Created on Aug 26, 2014

@author: demi
'''
from nap.net.net_monitor import NetMonitor


from nap.napclient import base

class NetMonitorResource(base.Resource):
    pass


class NetMonitorManager(base.ManagerWithFind):
    resource_class = NetMonitorResource
    
    def monitor_start(self):
        NetMonitor.monitor_start()
    
    def monitor_stop(self):
        NetMonitor.monitor_stop()
    
    def list(self):
        NetMonitor.show()
    
    def set(self,test_ip,default_gw, switch_gw):
        NetMonitor.set(test_ip, default_gw, switch_gw)
    
    def show(self,server):
        pass
    

if __name__ == '__main__':
    pass