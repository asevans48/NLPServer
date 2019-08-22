"""
AIO Http server entry point for NLP tasks

@author aevans
"""

from aiohttp import web
import json


async def handle_ner_request(request):
    json_out = ""
    return web.Response(text=json_out)


async def handle_text_segmentation_request(request):
    json_out = ""
    return web.Response(text=json_out)


async def handle_read_me_request(request):
    read_me_out = ""
    return web.Response(text=read_me_out)


app = web.Application()
app.router.add_get('/', handle_read_me_request)
app.router.add_post('/text_segment', handle_text_segmentation_request)
app.router.add_post('/named_entity_recognition', handle_ner_request)
