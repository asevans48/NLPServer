"""
The NER task.

@author Andrew Evans
"""

import json

import celery

from nlp_server.nlp.named_entity_recognition import NERModel
from nlp_server.cache import cache_ops


class NERTask(celery.Task):
    """
    NER task for celery
    """

    name = 'NERTask'
    _ner = None

    @property
    def ner(self):
        """
        Get the tokenizer. Set it if it is null.

        :return:    The tokenizer
        """
        client = cache_ops.get_redis()
        if self._ner is None:
            config_str = client.get('ner_config')
            print(config_str)
            if config_str:
                config = dict(json.loads(config_str))
                load_gpu = config.get('use_gpu', False)
                model_type = config.get('ner_model', 'en_core_web_sm')
                self._ner = NERModel(model_type, load_gpu)
            else:
                self._ner = NERModel('en_core_web_sm', False)
        return self._ner

    def get_entities(self, text, entity_types):
        """
        Get entities for a given text
        :param text:  The text string
        :param entity_types:    Entity types to recognize
        :return: Discovered entities dict
        """
        entities = {}
        self.ner.parse_text(text)
        for entity in entity_types:
            if entity == "PERSON":
                people = self.ner.get_people()
                entities['people'] = people
            elif entity == "LOCATION":
                locations = self.ner.get_language()
                entities['location'] = locations
            elif entity == "ORGANIZATION":
                organizations = self.ner.get_organizations()
                entities['organizations'] = organizations
            elif entity == "FACILITY":
                facs = self.ner.get_fac()
                entities['fac'] = facs
            elif entity == "LANGUAGE":
                langs = self.ner.get_language()
                entities['languages'] = langs
            elif entity == "DATE":
                dates = self.ner.get_date()
                entities['dates'] = dates
            elif entity == "EVENT":
                events = self.ner.get_events()
                entities['events'] = events
            elif entity == "PRODUCT":
                products = self.ner.get_product()
                entities['products'] = products
        return entities

    def run(self, text, entity_types):
        """
        Run the task

        :param text:    The text to recognize entities in
        :param entity_types:    The list of entity types to find
        :return:    A list of parsed entities
        """
        rval = []
        if type(text) is str:
            entities = self.get_entities(text, entity_types)
            rval.append(entities)
        elif type(text) is list:
            for text_str in text:
                entities = self.get_entities(text_str, entity_types)
                rval.append(entities)
        return rval
