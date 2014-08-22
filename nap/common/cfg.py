#coding:utf-8
'''
Created on Aug 22, 2014

@author: demi
'''
import os
import sys

from nap.lib.configobj import ConfigObj
from nap.lib.validate import Validator

from nap.utils import env


class Config(object):
    
    def __init__(self):
        self.pythonPath = env.cur_file_dir()
        self.configfile = self.pythonPath+"/nap/nap.conf"
        self.configspec = self.pythonPath+"/nap/conf/netswap.confspec"
        self.swapfile = self.pythonPath+"/nap/conf/nap.status"
        self._setup(self.configfile, self.configspec, self.swapfile)
    
    def _setup(self,configfile,configspec,swapfile):
        ""
        if not os.path.isfile(self.swapfile):
            os.popen("/bin/echo swap = False > "+self.swapfile)
        
        self.swap_status = ConfigObj(self.swapfile,encoding='UTF8')
        self.isSwap = self.swap_status["swap"]
        
        if not os.path.isfile(self.configfile):
            print "file "+self.configfile+" not exist."
            sys.exit()
    
        self.config = ConfigObj(self.configfile,configspec=self.configspec,encoding='UTF8')
        val = Validator()
        test = self.config.validate(val)
        if not test == True:
            print "Configuration file parameters errors"
            exit()
    
    
    def get_sections(self):
        return self.config.keys()
    
    def get_section(self,section_name):
        return self.config[section_name]
    
    def list(self):
        for i in self.__dict__ :
            print i+" : "+self.__dict__[i]


CONF = Config()

if __name__ == '__main__':
    pass