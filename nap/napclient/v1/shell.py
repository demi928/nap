#coding:utf-8
'''
Created on Aug 25, 2014

@author: demi
'''

from nap.napclient import utils
from nap.napclient import logger

@utils.arg('server', metavar='<server>', help=('Name or ID of server.'))
def do_list(cs, args):
    """List Nap."""
    print "dd"
    logger.debug("list")

if __name__ == '__main__':
    pass