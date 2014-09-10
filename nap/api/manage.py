#coding:utf-8
'''
Created on Aug 27, 2014

@author: demi
'''


from webob import Request
from webob import Response



class ShowVersion(object):
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



if __name__ == '__main__':
    pass