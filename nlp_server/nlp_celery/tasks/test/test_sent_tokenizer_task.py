"""
Test the sent tokenizer

@author Andrew Evans
"""

from nlp_server.nlp_celery.tasks.sent_tokenizer_task import SentTokenizerTask


def test_get_tokenizer():
    """
    Test obtaining the tokenizer
    """
    tok = SentTokenizerTask()
    tokenizer = tok.tokenizer
    assert tokenizer


def test_run_tokenizer():
    """
    Test running the tokenizer
    """
    tok = SentTokenizerTask()
    txt = """This is the first sentence. This is the second!"""
    sents = tok.run(txt)
    print(sents)
    assert(type(sents) is dict)
    assert(sents.get('err', True) is False)
    assert(sents.get('sentences', None) is not None)
    assert(len(sents['sentences']) == 1)
    assert(len(sents['sentences'][0]) == 2)
