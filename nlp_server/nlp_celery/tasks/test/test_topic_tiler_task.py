"""
Test the topic tiler

@author Andrew Evans
"""

from nlp_server.nlp_celery.tasks.topic_tiler_task import TopicTilerTask


def test_get_tokenizer():
    """
    Obtain the tokenizer
    """
    tiler = TopicTilerTask()
    tokenizer = tiler.tokenizer
    assert tokenizer


def test_tokenize_topics():
    """
    Test running the topic tiling
    """
    tiler = TopicTilerTask()
    txt = """
    Every task must have a unique name.

    If no explicit name is provided the task decorator will generate one
    for you, and this name will be based on 1) the module the task is 
    defined in, and 2) the name of the task function.
    +
    Example setting explicit name.
    
    The eager mode enabled by the task_always_eager setting is by definition
    not suitable for unit tests.

    When testing with eager mode you are only testing an emulation of what
    happens in a worker, and there are many discrepancies between the emulation
    and what happens in reality.
    """
    topics = tiler.run(txt)
    assert(type(topics) is dict)
    assert(topics.get('err', True) is False)
    assert(topics.get('segments', None) is not None)
    print(topics)
    assert(len(topics['segments']) == 1)
    assert(len(topics['segments'][0]) > 0)
