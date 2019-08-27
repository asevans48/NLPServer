"""
Sentence tokenization

@author Andrew Evans
"""

import celery

from nlp_server.nlp.sent_tokenize import SentenceTokenizer


class SentTokenizerTask(celery.Task):
    """
    Sent tokenizer task
    """
    _config = None
    _tokenizer = None

    @property
    def config(self):
        """
        Property getter for config
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Setter for config.

        :param config:  configuration class
        :return:    The config
        """
        self._config = config

    @property
    def tokenizer(self):
        """
        Tokenizer getter
        :return:    The sentence tokenizer
        """
        if self._tokenizer is None and self._config is not None:
            self._tokenizer = SentenceTokenizer(
                self._config.sent_tokenizer_path)
        return self._tokenizer

    def run(self, text, config):
        """
        Run the task

        :param text:    The text to tokenize
        :param config:  The configuration dictionary
        :return:    A list of discovered sentences
        """
        if self.config is None:
            self.config = config
        return self.tokenizer.tokenize_sentences(text)
