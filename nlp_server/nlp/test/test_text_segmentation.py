"""
Test text segmentation

@author aevans
"""

import os

from nlp_server.nlp.text_segmentation import TopicTokenizer


def test_text_segmentation():
    tiler = TopicTokenizer()
    current_dir = os.path.curdir
    fpath = os.path.sep.join([current_dir, 'data', 'speech.txt'])
    with open(fpath) as fp:
        txt = fp.read()
    topics = tiler.get_boundaries(txt)
    assert(len(topics) > 0)
    assert(len(topics) == 40)
