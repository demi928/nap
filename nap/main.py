#coding:utf-8
import time

from paste.deploy import loadapp
from wsgiref.simple_server import make_server 

from nap.common.cfg import CONF

from nap.utils import shell
from nap.net.net_monitor import NetMonitor



def main():
    NetMonitor.start()
    
    config = "/root/nap/api-paste.ini"
    appname = "common"
    wsgi_app = loadapp("config:%s" % config, appname)
    server = make_server('0.0.0.0',9001,wsgi_app)
    server.serve_forever()
    

if __name__ == '__main__':
    main()
