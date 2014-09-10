#coding:utf-8
'''
Created on Aug 29, 2014

@author: demi
'''


from eventlet import event
from eventlet.support import greenlets as greenlet
from eventlet import hubs
import eventlet

evt = event.Event()

def waiter():
    print "about to wait"
    result = evt.wait()
    print 'waited for,',result


hub = hubs.get_hub()
g = eventlet.spawn(waiter)
g2 = eventlet.spawn(waiter)
eventlet.sleep(0)
evt.send('a')
eventlet.sleep(0)



if __name__ == '__main__':
    pass