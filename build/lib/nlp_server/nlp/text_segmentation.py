"""
Text tiling tokenizer

@author aevans
"""

from nltk.corpus import stopwords
from nltk.tokenize.texttiling import TextTilingTokenizer


class TopicTokenizer:
    """
    Text tiling tokenizer
    """

    def __init__(self, cutoff_policy='HC', stop_words=stopwords.words('english'), w=20, k=10):
        """
        Constructor
        """
        self.__stop_words = stop_words
        self.__cutoff_policy = cutoff_policy
        self.__w = w
        self.__k = k
        self.__tiler = TextTilingTokenizer(stopwords=stop_words, cutoff_policy=cutoff_policy, w=w, k=k)

    def get_boundaries(self, text):
        """
        Get potential topic boundaries between the text.

        :param text:    The text to tile
        :return:    A list of potential topics
        """
        topics = self.__tiler.tokenize(text)
        return topics

    def reload_tiler(self):
        """
        Reload the text tiler. Use if memory is an issue.
        """
        del self.__tiler
        self.__tiler = self.__tiler = TextTilingTokenizer(stopwords=self.__stop_words, cutoff_policy=self.__cutoff_policy, w=self.__w, k=self.__k)
