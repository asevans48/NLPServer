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

from nlp_server.nlp_celery.ner_task import NERTask
from nlp_server.nlp_celery.sent_tokenizer_task import SentenceTokenizer
from nlp_server.nlp_celery.topic_tiler_task import TopicTokenizer


if __name__ == "__main__":
    app = Celery('nlp_server')
    app.register_task(NERTask)
    app.register_task(SentenceTokenizer)
    app.register_task(TopicTokenizer)
    app.worker_main()
