#coding:utf-8
'''
Created on Aug 25, 2014

@author: demi
'''
from nap.napclient import utils

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

if __name__ == '__main__':
    pass