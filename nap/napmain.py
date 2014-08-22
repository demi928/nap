#!/usr/bin/env python
#coding:utf-8
import os
import sys
import re
import time

from nap.lib.configobj import ConfigObj
from nap.lib.validate import Validator

from nap.utils import shell
from nap.utils import env
from nap.common.cfg import CONF



def swap_net(gateway):
    global isSwap
    if isSwap == "True" :
        return isSwap

    swap_route(gateway)
    set_isSwap("True")

    return "swap_net"

def restore_net(gateway):
    global isSwap
    if isSwap == "False" :
        return isSwap
    
    swap_route(gateway)
    set_isSwap("False")
    
    return "restore_net"

def set_isSwap(status):
    global swap_status,isSwap
    swap_status["swap"] = status
    swap_status.write()
    isSwap = status
    
def swap_route(gateway):
#    online todo: demi 
        os.popen("/bin/stadmin -t %s" % gateway)
        os.popen("/sbin/route del default")
        os.popen("/sbin/route add default gw %s" % gateway)
    

pythonPath = CONF.pythonPath
configFile = CONF.configfile
configSpec = CONF.configspec
swapFile = CONF.swapfile
    
    
if not os.path.isfile(swapFile):
    os.popen("/bin/echo swap = False > "+swapFile)
    
swap_status = ConfigObj(swapFile,encoding='UTF8')
isSwap = swap_status["swap"]

def main():

    if not os.path.isfile(configFile):
        print "file "+configFile+" not exist."
        sys.exit()
    
    config = ConfigObj(configFile,configspec=configSpec,encoding='UTF8')
    val = Validator()
    test = config.validate(val)
    if not test == True:
        print "Configuration file parameters errors"
        exit()
    
      
    section = config["main"]
    
        
    while True:
        result = shell.test_ping(section["ip1"])
        if result :
            restore_net(section["gateway1"])
        else:
            swap_net(section["gateway2"])
        time.sleep(3)

if __name__ == '__main__':
    main()
