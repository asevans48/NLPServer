"""
Test the named entity recognition system

@author aevans
"""

from nlp_server.nlp.named_entity_recognition import NERModel


def test_parse_people():
    """
    Test parsing people from text
    """
    text = "John Doe is from Atlanta but Bill is from Detroit"
    ner = NERModel("en_core_web_sm", False)
    doc = ner.parse_text(text)
    assert(doc)
    found_people = ner.get_people()
    assert len(found_people) > 0
    assert "John Doe" in found_people
    assert "Bill" in found_people
