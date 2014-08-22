#coding:utf-8
'''
Created on Aug 22, 2014

@author: root
'''
import sys
import os


def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path): 
        return path 
    elif os.path.isfile(path): 
        return os.path.dirname(path) 

if __name__ == '__main__':
    print cur_file_dir()