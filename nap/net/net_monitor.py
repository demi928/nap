#coding:utf-8
'''
Created on Aug 22, 2014

@author: demi
'''
import os
import time
import threading

from nap.common.cfg import CONF
from nap.common.log import logger
from nap.utils import shell


class NetMonitorClass(threading.Thread):  
    
    section = CONF.get_section("main")  
    isSwap = CONF.isSwap
    isRun = CONF.isRun
    test_ip = section["ip1"]
    default_gw = section["gateway1"]
    switch_gw = section["gateway2"]
   
    def __init__(self, name=None):  
        threading.Thread.__init__(self)  
        self.name = name  
        
    def run(self):
        self._run()
        
    def _run(self):
        while True:
            if CONF.swap_status["isRun"]:
                result = shell.test_ping(NetMonitorClass.test_ip)
                if result :
                    self._restore_net(NetMonitorClass.default_gw)
                else:
                    self._swap_net(NetMonitorClass.switch_gw)
                self.show()
                time.sleep(3)
            else:
                self.show()
                time.sleep(5)
                
        
    def _swap_net(self,gateway):
        if NetMonitorClass.isSwap == "True" :
            return 
    
        self._swap_route(gateway)
        self._set_isSwap("True")
    
        return "_swap_net"
    
    def _restore_net(self,gateway):
        if NetMonitorClass.isSwap == "False" :
            return 
        
        self._swap_route(gateway)
        self._set_isSwap("False")
        
        return "_restore_net"
    
    def _set_isSwap(self,status):
        CONF.swap_status["swap"] = status
        CONF.swap_status.write()
        NetMonitorClass.isSwap = status
        
        logger.debug("isSwap=%s" % NetMonitorClass.isSwap)
        
    def _swap_route(self,gateway):
            #  online todo: demi 
            os.popen("/bin/stadmin -t %s" % gateway)
            os.popen("/sbin/route del default")
            os.popen("/sbin/route add default gw %s" % gateway)
            
            logger.info("switch route to %s" % gateway)
      
    def monitor_start(self):
        NetMonitorClass.isRun = True
        CONF.swap_status["isRun"] = True
        CONF.swap_status.write()
        
    def monitor_stop(self):
        NetMonitorClass.isRun = False
        CONF.swap_status["isRun"] = False
        CONF.swap_status.write()
        
    def show(self,msg=""):
        for name,value in vars(NetMonitorClass).items():
            if isinstance(value,(str,bool,unicode)):
                print('%s : %s'%(name,value))
            
        print msg


    def set(self,test_ip,default_gw,switch_gw):
        NetMonitorClass.test_ip = test_ip
        NetMonitorClass.default_gw = default_gw
        NetMonitorClass.switch_gw = switch_gw
        
 
NetMonitor = NetMonitorClass("NetMonitor")
NetMonitor.setDaemon(True)


if __name__ == '__main__':
    pass
    