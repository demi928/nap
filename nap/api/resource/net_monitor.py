#coding:utf-8
'''
Created on Sep 10, 2014

@author: demi
'''
from nap.api import wsgi

class Controller(object):
    """The Consoles controller for the OpenStack API."""

    def __init__(self):
        pass


    def index(self, req):
        """Returns a list of consoles for this instance."""
        return {
            'name': "test",
            'properties': "test"
        }

    def create(self, req):
        """Creates a new console."""
        print "create"


    def show(self, req):
        """Shows in-depth information on a specific console."""
        print "show"

    def update(self, req):
        """You can't update a console."""
        print "update"

    def delete(self, req):
        """Deletes a console."""
        print "delete"

def create_resource():
    return wsgi.Resource(Controller())

if __name__ == '__main__':
    pass