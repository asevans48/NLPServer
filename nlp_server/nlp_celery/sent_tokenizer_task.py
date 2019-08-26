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

    def __init__(self, sent_model):
        """
        Constructor

        :param sent_model:  The sentence tokenization model
        """
        self.__sent_model = sent_model
        self.__tokenizer = SentenceTokenizer(self.__sent_model)

    def run(self, text, *args, **kwargs):
        """
        Run the task

        :param text:    The text to tokenize
        :param args:    The application args
        :param kwargs:  The application kwargs
        :return:    A list of discovered sentences
        """
        return self.__tokenizer.tokenize_sentences(text)