#coding:utf-8
'''
Created on Aug 22, 2014

@author: demi
'''
import os

from nap.common.cfg import CONF

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
    
def swap_route(gateway):
        #  online todo: demi 
        os.popen("/bin/stadmin -t %s" % gateway)
        os.popen("/sbin/route del default")
        os.popen("/sbin/route add default gw %s" % gateway)
  

if __name__ == '__main__':
    pass