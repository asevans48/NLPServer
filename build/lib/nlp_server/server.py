"""
NLP server.

Usage:
    server.py -c <cfg> | --configpath=<cfg>
    server.py -h | --help

Options:
  -c CFG | --configpath=CFG  The path to the configuraiton file
  -h --help  Show this help screen

"""

from aiohttp import web
from nlp_server.config import load_config
from docopt import docopt


async def handle_ner_request(request):
    """
    Handles request for named entity recognition processing

    :param request: the incoming request
    :return:    A response wrapping the returned entity json
    """
    json_out = ""
    return web.Response(text=json_out)


async def handle_text_segmentation_request(request):
    """
    Handles text segmentation

    :param request: The incoming request
    :return:    A response wrapping hte returned segment json
    """
    json_out = ""
    return web.Response(text=json_out)


async def handle_read_me_request(request):
    """
    Return the read me

    :param request: The incoming request
    :return:    The read me wrapped response
    """
    read_me_out = """
        <html>
            <body>
            </body>
        </html>
    """
    return web.Response(text=read_me_out)


if __name__ == "__main__":
    ARGUMENTS = docopt(__doc__, version='NLP Server 0.1')
    CONFIGPATH = ARGUMENTS.get('--configpath')

    try:
        PLEN = len(CONFIGPATH)
        assert(CONFIGPATH and PLEN > 0)
    except AssertionError as error:
        print("Configuration Path Must be Present")

    CONFIG = load_config.load_config(CONFIGPATH)
    load_gpu = False
    if CONFIG.use_gpu:
        load_gpu = True

    if CONFIGPATH:
        APP = web.Application()
        APP.router.add_get('/', handle_read_me_request)
        APP.router.add_post('/text_segment', handle_text_segmentation_request)
        APP.router.add_post('/named_entity_recognition', handle_ner_request)
        web.run_app(APP)
