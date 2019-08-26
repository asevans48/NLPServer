"""
Topic tiling task

@author Andrew Evans
"""

import celery

from nlp_server.nlp.text_segmentation import TopicTokenizer


class TopicTilerTask(celery.task):

    def __init__(self, k, w, stopwords, cutoff_policy):
        """
        Constructor

        :param k:   Size of hte block for comparison
        :param w:   Pseudosentence width
        :param stopwords:   Stopword list
        :param cutoff_policy:   Algorithm for text boundaries
        """
        self.__k = k
        self.__w = w
        self.__stopwords = stopwords
        self.__cutoff_policy = cutoff_policy
        self.__tokenizer = TopicTokenizer(
            self.__cutoff_policy, self.__stopwords, self.__w, self.__k)

    def run(self, text, *args, **kwargs):
        """
        Obtain potential topics from the text.

        :param text:    The text to segment
        :param args:    Task arguments
        :param kwargs:  Task kwargs
        :return:    A list of segmented text topics
        """
        return self.__tokenizer.get_boundaries(text)
