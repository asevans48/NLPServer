"""
Setup py
"""

from distutils.core import setup

setup(
    name='NLPserver',
    version='0.1',
    description='NLP Server',
    author='Andrew Evans',
    packages=[
        'nlp_server',
        'nlp_server.cache',
        'nlp_server.config',
        'nlp_server.nlp',
        'nlp_server.nlp_celery',
        'nlp_server.nlp_celery.config',
        'nlp_server.nlp_celery.tasks'],
)
