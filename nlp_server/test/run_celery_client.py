"""
Celery test app

Usage:
    celery_test.py
    celery_test.py -c <cfg> | --configpath=<cfg>
    celery_test.py -h | --help

Options:
  -n CONC | --concurrency=CONC  Concurrency Level
  -c CFG | --configpath=CFG  The path to the configuraiton file
  -h --help  Show this help screen

"""

from docopt import docopt
import logging

from nlp_server.cache import cache_ops
from nlp_server.nlp_celery.celery_app import setup_app, set_config
from nlp_server.nlp_celery.tasks.ner_task import NERTask
from nlp_server.nlp_celery.tasks.sent_tokenizer_task import SentTokenizerTask
from nlp_server.nlp_celery.tasks.topic_tiler_task import TopicTilerTask


if __name__ == "__main__":
    logging.info("Setting up Application")
    APP = setup_app()

    DOC = docopt(__doc__, version='NLP Server 0.1')
    CLIENT = cache_ops.get_redis()
    logging.info('Setting Config')
    set_config(DOC, CLIENT)
    logging.info("Registering Tasks")
    print(APP.tasks)
    logging.info("Sending to Celery")
    APP.send_task('NERTask', args=['My name is slim Shady and all you other slim shadys can.', ['PERSON']])
