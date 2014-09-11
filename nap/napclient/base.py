#coding:utf-8
'''
Created on Aug 25, 2014

@author: demi
'''

from nap.napclient import utils
from nap.napclient.client import client

class Resource(object):
    def __init__(self,manager):
        pass
    
class Manager(utils.HookableMixin):
    resource_class = None
    
    def __init__(self, api=None):
        self.client = client
        
    def _list(self, url):
        resp = self.client.get(url)
        return resp

    def _get(self, url):
        resp = self.client.get(url)
        return resp

    def _post(self, url, headers=None):
        body = self.client.post(url, headers=headers)
        return body

    def _put(self, url,headers=None):
        resp = self.client.put(url,headers=headers)
        return resp
        
    def _delete(self, url):
        return self.client.delete(url)
    

class ManagerWithFind(Manager):
    
    def find(self, **kwargs):
        pass
    
    def findall(self, **kwargs):
        pass

if __name__ == '__main__':
    pass