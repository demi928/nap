#coding:utf-8
'''
Created on Aug 27, 2014

@author: demi
'''


from webob import Request
from webob import Response

import routes
from paste.deploy import loadapp
from wsgiref.simple_server import make_server  


class ShowVersion(object):
      '''
      app
      '''
      def __init__(self,version):
          self.version = version
      def __call__(self,environ,start_response):
          res = Response()
          res.status = '200 OK'
          res.content_type = "text/plain"
          content = ["hello"]
          content.append("%s\n" % self.version)
          res.body = '\n'.join(content)
          return res(environ,start_response)
      @classmethod
      def factory(cls,global_conf,**kwargs):
          print 'factory'
          print "kwargs:",kwargs
          return ShowVersion(kwargs['version'])


class LogFilter(object):
      '''
      Log
      '''
      def __init__(self,app):
          self.app = app
      def __call__(self,environ,start_response):
          print "you can write log"
          return self.app(environ,start_response)
      @classmethod
      def factory(cls,global_conf,**kwargs):
          return LogFilter

config = "/root/nap/api-paste.ini"
appname = "common"
wsgi_app = loadapp("config:%s" % config, appname)
server = make_server('0.0.0.0',9001,wsgi_app)
server.serve_forever()

if __name__ == '__main__':
    pass