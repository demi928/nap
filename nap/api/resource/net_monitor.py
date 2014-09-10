#coding:utf-8
'''
Created on Sep 10, 2014

@author: demi
'''
from nap.api import wsgi
from nap.net.net_monitor import NetMonitor

class Controller(object):
    """The Consoles controller for the OpenStack API."""

    def __init__(self):
        pass


    def index(self, req):
        return NetMonitor.show()

    def create(self, req):
        NetMonitor.monitor_start()
        
        return "net-monitor start"

    def show(self, req,id):
        return NetMonitor.show()

    def update(self, req,id):
        test_ip = req.headers.get("test_ip")
        default_gw = req.headers.get("default_gw")
        switch_gw = req.headers.get("switch_gw")
        NetMonitor.set(test_ip, default_gw, switch_gw)
        
        return NetMonitor.show()

    def delete(self, req,id):
        NetMonitor.monitor_stop()
        return "net-monitor stop"

def create_resource():
    return wsgi.Resource(Controller())

if __name__ == '__main__':
    pass