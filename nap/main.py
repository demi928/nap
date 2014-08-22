#!/usr/bin/env python
#coding:utf-8
import os
import time
import sys
print sys.path

from nap.common.cfg import CONF
from nap.utils import shell
from nap.net import netswitch



def main():
    section = CONF.get_section("main")          
    while True:
        result = shell.test_ping(section["ip1"])
        if result :
            netswitch.restore_net(section["gateway1"])
        else:
            netswitch.swap_net(section["gateway2"])
        time.sleep(3)

if __name__ == '__main__':
    main()
