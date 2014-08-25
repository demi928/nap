#!/usr/bin/env python
#coding:utf-8
'''
Created on Aug 22, 2014

@author: demi
'''
import sys

from nap.main import main
from nap.napclient import shell
        

if __name__ == '__main__':
    sys.exit(shell.main())
#    sys.exit(main())