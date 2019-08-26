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


if __name__ == "__main__":
    app = Celery('nlp_server')
    app.worker_main()
