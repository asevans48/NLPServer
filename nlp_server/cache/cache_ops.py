"""
Cache functions

@author Andrew Evans
"""

import os

from pymemcache.client import base
import redis


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


def get_redis():
    """
    Get the redis cache client

    :return:    The redis cache client
    """
    host = os.environ.get('REDIS_HOST', 'localhost')
    port = os.environ.get('REDIS_PORT', 6379)
    password = os.environ.get('REDIS_PASSWORD', None)
    if password:
        redis_cli = redis.Redis(
            host=host,
            port=port,
            password=password
        )
    else:
        redis_cli = redis.Redis(
            host=host,
            port=port
        )
    return redis_cli
