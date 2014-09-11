#coding:utf-8
'''
Created on Sep 10, 2014

@author: demi
'''
import requests
import pprint

data = {
        'test_ip': '10.10.10.3',
        'default_gw': '172.16.0.254',
        'switch_gw': '172.16.0.254'
        }

r = requests.request('put','http://172.16.0.248:9001/v1/net_monitors/default',headers=data)

print r.text




if __name__ == '__main__':
    pass