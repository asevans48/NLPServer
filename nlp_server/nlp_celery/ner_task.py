"""
The NER task.

@author Andrew Evans
"""

import celery

from nlp_server.nlp_celery.celery_app import app
from nlp_server.nlp.named_entity_recognition import NERModel


class NERTask(celery.Task):
    """
    NER task for celery
    """

    def __init__(self, config):
        """
        Constructor

        :param config:  The configuration for the task
        """
        self.__config = config
        self.__model = self.__config.ner_model
        self.__is_gpu = self.__config.is_gpu
        self.__ner = NERModel(self.__model, self.__is_gpu)

    def run(self, text, entity_types, *args, **kwargs):
        """
        Run the task

        :param text:    The text to recognize entities in
        :param entity_types:    The list of entity types to find
        :param args:    Task arguments
        :param kwargs:  Task kwargs
        :return:    A dictionary containing the results separated by entities
        """
        entities = {}
        self.__ner.parse_text(text)
        for entity in entity_types:
            if entity == "PERSON":
                people = self.__ner.get_people(text)
                entities['people'] = people
            elif entity == "LOCATION":
                locations = self.__ner.get_language()
                entities['location'] = locations
            elif entity == "ORGANIZATION":
                organizations = self.__ner.get_organizations()
                entities['organizations'] = organizations
            elif entity == "FACILITY":
                facs = self.__ner.get_fac()
                entities['fac'] = facs
            elif entity == "LANGUAGE":
                langs = self.__ner.get_language()
                entities['languages'] = langs
            elif entity == "DATE":
                dates = self.__ner.get_date()
                entities['dates'] = dates
            elif entity == "EVENT":
                events = self.__ner.get_events()
                entities['events'] = events
            elif entity == "PRODUCT":
                products = self.__ner.get_product()
                entities['products'] = products
            return entities
