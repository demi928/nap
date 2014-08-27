#coding:utf-8
'''
Created on Aug 25, 2014

@author: demi
'''

from nap.napclient import utils
from nap.napclient import logger

def sub_net_monitor (cs, args):
    """net monitor module."""
    pass

def net_monitor_start(cs, args):
    """Start the net-monitor."""
    cs.net_monitor.monitor_start()
    
def net_monitor_stop(cs, args):
    """Stop the net-monitor."""
    cs.net_monitor.monitor_stop()
    
def net_monitor_list(cs, args):
    """List the net-monitor status."""
    cs.net_monitor.list()


@utils.arg('test_ip', metavar='<test_ip>', help=('test_ip.'))
@utils.arg('default_gw', metavar='<default_gw>', help=('default_gw.'))
@utils.arg('switch_gw', metavar='<switch_gw>', help=('switch_gw.'))
def net_monitor_set(cs, args):
    """ Set the net-monitor arguments"""
    cs.net_monitor.set(args.test_ip,args.default_gw,args.switch_gw)


@utils.arg('server', metavar='<server>', help=('Name or ID of server.'))
def net_monitor_show(cs, args):
    """Show details about the given server."""
    cs.net_monitor




    


if __name__ == '__main__':
    pass