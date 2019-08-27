"""
Cache functions

@author Andrew Evans
"""

import os

from pymemcache.client import base


def get_memcache():
    """
    Get the memcache client

    :return:    The memcache client
    """
    host = os.environ['MEMCACHE_HOST']
    port = os.environ['MEMCACHE_PORT']
    if host is None:
        host = '127.0.0.1'
    if port is None:
        port = 11211
    else:
        port = int(port)
    client = base.Client((host, port))