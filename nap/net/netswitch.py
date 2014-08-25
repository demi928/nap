#coding:utf-8
'''
Created on Aug 22, 2014

@author: demi
'''
import os
import time

from nap.common.cfg import CONF
from nap.common.log import logger
from nap.utils import shell

isSwap = CONF.isSwap

def swap_net(gateway):
    global isSwap
    if isSwap == "True" :
        return 

    swap_route(gateway)
    set_isSwap("True")

    return "swap_net"

def restore_net(gateway):
    global isSwap
    if isSwap == "False" :
        return 
    
    swap_route(gateway)
    set_isSwap("False")
    
    return "restore_net"

def set_isSwap(status):
    global isSwap
    CONF.swap_status["swap"] = status
    CONF.swap_status.write()
    isSwap = status
    
    logger.debug("isSwap=%s" % isSwap)
    
def swap_route(gateway):
        #  online todo: demi 
        os.popen("/bin/stadmin -t %s" % gateway)
        os.popen("/sbin/route del default")
        os.popen("/sbin/route add default gw %s" % gateway)
        
        logger.info("switch route to %s" % gateway)
  
def main():
    section = CONF.get_section("main")          
    while True:
        result = shell.test_ping(section["ip1"])
        if result :
            restore_net(section["gateway1"])
        else:
            swap_net(section["gateway2"])
        time.sleep(3)

if __name__ == '__main__':
    pass