"""
Topic tiling task

@author Andrew Evans
"""

import json
import traceback

import celery
from nltk.corpus import stopwords

from nlp_server.cache import cache_ops
from nlp_server.nlp.text_segmentation import TopicTokenizer


class TopicTilerTask(celery.Task):
    """
    Topic Tiler Task
    """

    name = 'TextTilingTokenizer'
    _tokenizer = None

    @property
    def tokenizer(self):
        """
        Get the tokenizer. Set it if it is null.

        :return:    The tokenizer
        """
        config = cache_ops.get_redis()
        if self._tokenizer is None:
            cfg_str = config.get('topic_tiler_config')
            if cfg_str:
                cfg = dict(json.loads(cfg_str))
                width = int(cfg.get('w', 20))
                k_size = int(cfg.get('k', 10))
                stop_words = cfg.get('stopwords', 'english')
                stop_words = stopwords.words(stop_words)
                cutoff_policy = cfg.get('cutoff_policy', 'HC')
            else:
                width = 20
                k_size = 10
                stop_words = 'english'
                stop_words = stopwords.words(stop_words)
                cutoff_policy = 'HC'
            self._tokenizer = TopicTokenizer(
                cutoff_policy, stop_words, width, k_size)
        return self._tokenizer

    def get_topic_segements(self, text):
        """
        Obtain a list of topic segments
        :param text:    The text to segment
        :return:    A list of segmented text
        """
        return self.tokenizer.get_boundaries(text)

    def run(self, text):
        """
        Obtain potential topics from the text.

        :param text:    The text to segment or list of texts
        :return:    Lists of segmented text topics
        """
        rval = []
        try:
            if type(text) is str:
                segments = self.get_topic_segements(text)
                rval.append(segments)
            elif type(text) is list:
                for text_str in text:
                    segments = self.get_topic_segements(text_str)
                    rval.append(segments)
        except Exception as e:
            traceback.print_exc()
        return rval
