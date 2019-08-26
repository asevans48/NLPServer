"""
Test sentence tokenization

@author Andrew Evans
"""

from nlp_server.nlp.sent_tokenize import SentenceTokenizer


def test_sentence_tokenizer():
    tokenizer = SentenceTokenizer('tokenizers/punkt/english.pickle')
    test_text = "The dog is grey. The sky is blue."
    sents = tokenizer.tokenize_sentences(test_text)
    assert(len(sents) == 2)
