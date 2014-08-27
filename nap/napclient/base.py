#coding:utf-8
'''
Created on Aug 25, 2014

@author: demi
'''

from nap.napclient import utils

class Resource(object):
    def __init__(self,manager):
        pass
    
class Manager(utils.HookableMixin):
    resource_class = None
    
    def __init__(self, api):
        self.api = api

class ManagerWithFind(Manager):
    
    def find(self, **kwargs):
        pass
    
    def findall(self, **kwargs):
        pass

if __name__ == '__main__':
    pass