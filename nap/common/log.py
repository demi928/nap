#coding:utf-8
'''
Created on Aug 22, 2014

@author: demi
'''

import logging.config

from nap.common.cfg import CONF

class Log(object):


    def __init__(self):
        ""
        logging.config.fileConfig(CONF.logConfigFile)
        self.logger = logging.getLogger()
        
    def reload(self):
        logging.config.fileConfig(CONF.logConfigFile)
        self.logger = logging.getLogger()
        
    def get_logger(self):
        return self.logger
    
    def get_loggerWithName(self,name):
        return logging.getLogger(name)
    
LOG = Log()
logger = LOG.get_logger()

logger.debug("The nap config info : \n"+CONF.__dict__.__repr__())

if __name__ == '__main__':
    pass