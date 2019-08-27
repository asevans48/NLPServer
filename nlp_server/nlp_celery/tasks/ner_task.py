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
    _ner = None

    @property
    def ner(self):
        """
        Get the tokenizer. Set it if it is null.

        :return:    The tokenizer
        """
        client = cache_ops.get_memcache()
        if self._ner is None:
            config_str = client.get('ner_config')
            if config_str:
                config = dict(json.loads(config_str))
                load_gpu = config.get('use_gpu')
                model_type = config.get('model_type')
                self._ner = NERModel(model_type, load_gpu)

    def run(self, text, entity_types, config):
        """
        Run the task

        :param text:    The text to recognize entities in
        :param entity_types:    The list of entity types to find
        :param config:  The configuration
        :return:    A dictionary containing the results separated by entities
        """
        entities = {}
        self.ner.parse_text(text)
        for entity in entity_types:
            if entity == "PERSON":
                people = self.ner.get_people(text)
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
