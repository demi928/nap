#coding:utf-8
'''
Created on Aug 26, 2014

@author: demi
'''



from nap.napclient import base

class NetMonitorResource(base.Resource):
    pass


class NetMonitorManager(base.ManagerWithFind):
    resource_class = NetMonitorResource
    
    def monitor_start(self):
        pass
    
    def monitor_stop(self):
        pass
    
    def list(self):
        pass
    
    def set(self,test_ip,default_gw, switch_gw):
        pass
    
    def show(self,server):
        pass
    

if __name__ == '__main__':
    pass