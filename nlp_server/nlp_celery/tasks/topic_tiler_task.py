"""
Topic tiling task

@author Andrew Evans
"""

import json

import celery
from nltk.corpus import stopwords

from nlp_server.cache import cache_ops
from nlp_server.nlp.text_segmentation import TopicTokenizer


class TopicTilerTask(celery.Task):
    """
    Topic Tiler Task
    """

    name = 'Text Tiling Tokenizer'
    _tokenizer = None

    @property
    def tokenizer(self):
        """
        Get the tokenizer. Set it if it is null.

        :return:    The tokenizer
        """
        config = cache_ops.get_memcache()
        if self._tokenizer is None:
            cfg_str = config.get('topic_tiler_config')
            cfg = dict(json.loads(cfg_str))
            width = int(cfg.get('w', 20))
            k_size = int(cfg.get('k', 10))
            stop_words = cfg.get('stopwords', 'english')
            stop_words = stopwords.words(stop_words)
            cutoff_policy = cfg.get('cutoff_policy', 'HC')
            self._tokenizer = TopicTokenizer(
                cutoff_policy, stop_words, width, k_size)

    def run(self, text, config):
        """
        Obtain potential topics from the text.

        :param text:    The text to segment
        :param config:  The configuration dictionary
        :return:    A list of segmented text topics
        """
        if self.config is None:
            self.config = config
        return self._tokenizer.get_boundaries(text)
