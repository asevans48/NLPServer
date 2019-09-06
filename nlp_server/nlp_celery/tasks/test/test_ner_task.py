"""
Test celery ner

@author Andrew Evans
"""

from nlp_server.nlp_celery.tasks.ner_task import NERTask


def test_get_ner():
    """
    Test obtaining the ner tokenizer
    """
    ner_cls = NERTask()
    ner = ner_cls.ner
    assert ner


def test_ner_run():
    """
    Test running the named entity recognizer
    """
    txt = "My name is Joe. I am a person."
    ner_cls = NERTask()
    result = ner_cls.run(txt, ["PERSON"])
    assert len(result > 0)
    assert 'people' in result[0].keys()
    assert 'Joe' in result[0].get('people')
