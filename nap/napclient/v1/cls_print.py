#coding:utf-8
'''
Created on Sep 11, 2014

@author: demi
'''

from nap.napclient import utils

def print_monitor_list(dic):
    fields = [
        'Test IP',
        'Default GW',
        'Switch GW',
        'Is Running',
        'Is Switch'
    ]
    
    utils.print_dict_horizon(dic,fields)

if __name__ == '__main__':
    pass