#coding:utf-8
'''
Created on Sep 10, 2014

@author: demi
'''
import requests
import pprint

r = requests.request('get','http://172.16.0.248:9001/v1/net_monitors/default')

pprint.pprint(r.json())


if __name__ == '__main__':
    pass