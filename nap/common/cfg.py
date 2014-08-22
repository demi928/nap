#coding:utf-8
'''
Created on Aug 22, 2014

@author: demi
'''

from nap.utils import env


class Config(object):
    
    def __init__(self):
        self.pythonPath = env.cur_file_dir()
        self.configfile = self.pythonPath+"/nap.conf"
        self.configspec = self.pythonPath+"/conf/netswap.confspec"
        self.swapfile = self.pythonPath+"/conf/is_swap.status"
    
    def list(self):
        for i in self.__dict__ :
            print i+" : "+self.__dict__[i]


CONF = Config()

if __name__ == '__main__':
    for i in CONF.__dict__ :
        print i+" : "+CONF.__dict__[i]