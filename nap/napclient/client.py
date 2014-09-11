#coding:utf-8
'''
Created on Aug 25, 2014

@author: demi
'''
import requests

from nap.napclient import utils

class HTTPClient(object):
    def __init__(self):
        pass
    
    def request(self, url, method, **kwargs):
        resp = requests.request(
            method,
            url,
            **kwargs)
        
        return resp
    
    def get(self, url, **kwargs):
        return self.request(url, 'GET', **kwargs)

    def post(self, url, **kwargs):
        return self.request(url, 'POST', **kwargs)

    def put(self, url, **kwargs):
        return self.request(url, 'PUT', **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, 'DELETE', **kwargs)
    

def get_client_class(version):
    version_map = {
        '1': 'nap.napclient.v1.client.Client',
    }
    try:
        client_path = version_map[str(version)]
    except (KeyError, ValueError):
        msg = _("Invalid client version '%(version)s'. must be one of: "
                "%(keys)s") % {'version': version,
                               'keys': ', '.join(version_map.keys())}
        raise Exception(msg)

    return utils.import_class(client_path)

def Client(version, *args, **kwargs):
    client_class = get_client_class(version)
    return client_class(*args, **kwargs)

client = HTTPClient()

if __name__ == '__main__':
    pass