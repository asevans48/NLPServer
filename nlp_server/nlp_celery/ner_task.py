"""
The NER task.

@author Andrew Evans
"""

import celery

from nlp_server.nlp_celery.celery_app import app


class NERTask(celery.Task):
    """
    NER task for celery
    """
    NERMODEL = None
    TOPICTILER = None

    def __init__(self, config):
        self.config = config

    def run(self, *args, **kwargs):
        """
        Run the task
        :param args:
        :param kwargs:
        :return:
        """
