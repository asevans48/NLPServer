"""
Celery starting point.

Usage:
    server.py -c <cfg> | --configpath=<cfg>
    server.py -h | --help

Options:
  -c CFG | --configpath=CFG  The path to the configuraiton file
  -h --help  Show this help screen

"""

from celery import Celery
from docopt import docopt
import json

from nlp_server.cache import cache_ops
from nlp_server.nlp_celery.ner_task import NERTask
from nlp_server.nlp_celery.sent_tokenizer_task import SentenceTokenizer
from nlp_server.nlp_celery.topic_tiler_task import TopicTokenizer


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
    APP = Celery('nlp_server')

    DOC = docopt(__doc__, version='NLP Server 0.1')
    CLIENT = cache_ops.get_memcache()
    set_config(DOC, CLIENT)

    APP.register_task(NERTask)
    APP.register_task(SentenceTokenizer)
    APP.register_task(TopicTokenizer)
    APP.worker_main()
