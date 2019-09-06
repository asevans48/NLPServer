"""
Sentence tokenization

@author Andrew Evans
"""

import json

import celery

from nlp_server.cache import cache_ops
from nlp_server.nlp.sent_tokenize import SentenceTokenizer


class SentTokenizerTask(celery.Task):
    """
    Sent tokenizer task
    """
    name = 'Sentence Tokenizer'
    _tokenizer = None

    @property
    def tokenizer(self):
        """
        Tokenizer getter
        :return:    The sentence tokenizer
        """
        config = cache_ops.get_redis()
        if self._tokenizer is None:
            cfg_str = config.get('sent_tokenizer_config')
            cfg = dict(json.loads(cfg_str))
            tok_path = cfg.get('sent_tokenizer_path')
            self._tokenizer = SentenceTokenizer(tok_path)
        return self._tokenizer

    def tokenize_text(self, text):
        """
        Tokenize a text string
        :param text:    text string
        :return:    List of sentences
        """
        return self.tokenizer.tokenize_sentences(text)

    def run(self, text):
        """
        Run the task

        :param text:    The text to tokenize or list of texts
        :return:    A list of discovered sentences
        """
        rval = []
        if type(text) is str:
            sents = self.tokenizer.tokenize_sentences(text)
            rval.append(sents)
        elif type(text) is list:
            for text_str in text:
                sents = self.tokenizer.tokenize_sentences(text_str)
                rval.append(sents)
        return rval
