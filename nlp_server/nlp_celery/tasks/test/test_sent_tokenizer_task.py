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
    assert(len(sents) == 1)
    assert(len(sents[0]) == 2)
