#coding:utf-8
'''
Created on Aug 28, 2014

@author: demi
'''
from nap.api import wsgi
from nap.api.resource import net_monitor


class MyRouterApp(wsgi.Router):
    def __init__(self,mapper):
        self.resources = {}
        self._setup_routes(mapper)
        super(MyRouterApp, self).__init__(mapper)
        
        
    def _setup_routes(self,mapper):
        self.resources['net_monitor'] = net_monitor.create_resource()
        mapper.resource("net_monitor", "net_monitors",
                    controller=self.resources['net_monitor'])



if __name__ == '__main__':
    pass