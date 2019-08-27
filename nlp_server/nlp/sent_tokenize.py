"""
Sentence tokenization

@author Andrew Evans
"""

import nltk

from pymemcache.client import base


class SentenceTokenizer:
    """
    Sentence based tokenization
    """

    def __init__(self, model_path):
        """
        Constructor

        :param model_path:  Model path for sentence tokenization
        """
        self.__tokenizer = nltk.data.load(model_path)

    def reset_model(self, model_path):
        """
        Reset the base model

        :param model_path:  Model path for sentence tokenization
        """
        self.__tokenizer = nltk.load(model_path)

    def tokenize_sentences(self, text):
        """
        Tokenizer

        :param text:    The text to tokenize
        :return:    A list of discovered distances
        """
        return self.__tokenizer.tokenize(text)
