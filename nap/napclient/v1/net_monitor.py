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
    base_http_path = "http://172.16.0.248:9001/v1"
    monitor_path = "/net_monitors"
    url = base_http_path+monitor_path
    
    def monitor_start(self):
        resp = self._post(NetMonitorManager.url)
        return resp
    
    def monitor_stop(self):
        resp = self._delete(NetMonitorManager.url+"/default")
        return resp
    
    def list(self): 
        resp = self._list(NetMonitorManager.url)
        return resp
    
    def set(self,test_ip,default_gw, switch_gw):
        headers = {
            'test_ip': test_ip,
            'default_gw': default_gw,
            'switch_gw': switch_gw
        }
        resp = self._put(NetMonitorManager.url+"/default",headers)
        return resp
    
    def show(self,server="default"):
        resp = self._get(NetMonitorManager.url+"/"+server)
        return resp
    

if __name__ == '__main__':
    pass