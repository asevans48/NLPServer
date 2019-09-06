"""
Celery starting point.

Usage:
    celery_app.py
    celery_app.py -c <cfg> | --configpath=<cfg>
    celery_app.py -h | --help

Options:
  -n CONC | --concurrency=CONC  Concurrency Level
  -c CFG | --configpath=CFG  The path to the configuraiton file
  -h --help  Show this help screen

"""

import logging
import json
import os

from celery import Celery
from docopt import docopt

from nlp_server.cache import cache_ops
from nlp_server.nlp_celery.tasks.ner_task import NERTask
from nlp_server.nlp_celery.tasks.sent_tokenizer_task import SentTokenizerTask
from nlp_server.nlp_celery.tasks.topic_tiler_task import TopicTilerTask


def get_config():
    """
    Obtain the celery config

    :return:    The configuration jsonj
    """
    cfg_path = os.environ.get("NLP_CELERY_CONFIG")
    if cfg_path is None:
        cdir = os.path.curdir
        cfg_path = os.path.sep.join([cdir, 'config', 'default.json'])
    with open(cfg_path, 'r') as fp:
        cfg = dict(json.load(fp))
    return cfg


def setup_app():
    """
    Setup the celery app

    :return:    The celery app
    """
    cfg = get_config()
    backend = cfg['backend']
    print(backend)
    broker = cfg['broker']
    app = Celery('nlp_server', broker=broker, backend=backend)

    if cfg.get('task_serializer'):
        app.conf.task_serializer = cfg.get('task_serializer')

    if cfg.get('rseult_serializer'):
        app.conf.result_serializer = cfg.get('result_serializer')

    if cfg.get('accept_content'):
        app.conf.accept_content = cfg.get('accept_content')

    if cfg.get('worker_prefetch_multiplier'):
        app.conf.worker_prefetch_multiplier = int(
            cfg.get('worker_prefetch_multiplier'))
    return app


def set_config(doc, client):
    """
    Set the config path

    :param doc: The document path
    :param client:  The memcached config
    """
    if doc.get('CONFIGPATH'):
        cfg_path = doc.get('CONFIGPATH')
        with open(cfg_path, 'r') as fp:
            cfg = dict(json.load(fp))
        if cfg and cfg.get('ner'):
            ner_jsn = json.dumps(cfg.get('ner'))
            client.set('ner_config', ner_jsn)

        if cfg and cfg.get('sent_tokenizer'):
            sent_jsn = json.dumps(cfg.get('sent_tokenizer'))
            client.set('sent_tokenizer_config', sent_jsn)

        if cfg and cfg.get('topic_segmentation'):
            topic_jsn = json.dumps(cfg.get('text_segmentation'))
            client.set('topic_tiler_config', topic_jsn)


if __name__ == "__main__":
    logging.info("Setting up Application")
    APP = setup_app()

    DOC = docopt(__doc__, version='NLP Server 0.1')
    CLIENT = cache_ops.get_redis()
    logging.info('Setting Config')
    set_config(DOC, CLIENT)
    logging.info("Registering Tasks")
    APP.tasks.register(NERTask())
    APP.tasks.register(SentTokenizerTask())
    APP.tasks.register(TopicTilerTask())
    print(APP.tasks)
    logging.info("Starting Celery")
    argv = [
        'worker',
        '--pool=gevent',
        '--loglevel=INFO'
    ]
    conc_level = DOC.get('concurrency', 1)
    conc_level = "--concurrency={}".format(conc_level)
    argv.append(conc_level)
    print("ATTEMPTING RUN")
    APP.worker_main(argv)
