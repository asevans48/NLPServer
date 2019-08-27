"""
Topic tiling task

@author Andrew Evans
"""

import celery

from nlp_server.nlp.text_segmentation import TopicTokenizer


class TopicTilerTask(celery.Task):
    """
    Topic Tiler Task
    """
    _config = None
    _tokenizer = None

    @property
    def config(self):
        """
        Obtain the config

        :return:    The config dictionary
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Set the config

        :param config:  The config
        """
        self._config = config

    @property
    def tokenizer(self):
        """
        Get the tokenizer. Set it if it is null.

        :return:    The tokenizer
        """
        if self._tokenizer is None:
            width = self._config.w
            k_size = self._config.k
            stopwords = self._config.stopwords
            cutoff_policy = self._config.cutoff_policy
            self._tokenizer = TopicTokenizer(
                cutoff_policy, stopwords, width, k_size)

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
