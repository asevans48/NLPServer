"""
Named entity recognition.

@author Andrew Evans
"""

import spacy


class NERModel:
    """
    NER Model object with functions
    """

    def __init__(self, model_type, load_gpu=False):
        """
        Constructor

        :param model_type:  Path to the model
        :param load_gpu:    Whether to use gpu processing
        """
        self.__is_gpu = False
        if load_gpu:
            self.__is_gpu = spacy.require_gpu()
        self.__nlp = spacy.load(model_type)
        self.__document = None

    def is_gpu(self):
        """
        Whether gpus are available for processing

        :return:    Whether gpus are available
        """
        return self.__is_gpu

    def load_gpu(self):
        """
        If gpus are not loaded, try to load them

        :return:    Whether gpus were loaded
        """
        if self.__is_gpu is False:
            self.__is_gpu = spacy.require_gpu()
        return self.__is_gpu

    def get_people(self):
        """
        Get potential people from a text string.

        :param doc: The document to process
        :return:    A list of people
        """
        people = []
        if self.__document:
            for ent in self.__document.ents:
                if ent.label_.upper() == 'PERSON':
                    people.append(ent.text)
        return people

    def get_money(self):
        """
        Get monetary values with units.

        :return:    A list of potential monetary units
        """
        monies = []
        if self.__document:
            for ent in self.__document.ents:
                if ent.label_.upper() == 'MONEY':
                    monies.append(ent.text)
        return monies

    def get_date(self):
        """
        Get dates from a text document

        :return:    A list of potential dates
        """
        dates = []
        if self.__document:
            for ent in self.__document.ents:
                lbl = ent.label_.upper()
                if lbl == 'DATE' or lbl == 'TIME':
                    dates.append(ent.text)
        return dates

    def get_fac(self):
        """
        Get potential facilities and places from text

        :return:    A list of potential places and facilities
        """
        facs = []
        if self.__document:
            for ent in self.__document.ents:
                lbl = ent.label_.upper()
                if lbl == 'FAC':
                    facs.append(ent.text)
        return facs

    def get_events(self):
        """
        Get potential events from text

        :return:    A list of potential events
        """
        events = []
        if self.__document:
            for ent in self.__document.ents:
                lbl = ent.label_.upper()
                if lbl == 'EVENT':
                    events.append(ent.text)
        return events

    def get_locations(self):
        """
        Get locations from a text string

        :param doc: The document to process
        :return:    A list of locations
        """
        locations = []
        if self.__document:
            for ent in self.__document.ents:
                lbl = ent.label_.upper()
                if lbl == 'GPE' or lbl == 'LOC':
                    locations.append(ent.text)
        return locations

    def get_organizations(self):
        """
        Get organizations from a text string

        :param doc: The document to process
        :return:    A list of organizations
        """
        orgs = []
        if self.__document:
            for ent in self.__document.ents:
                lbl = ent.label_.upper()
                if lbl == 'ORG' or lbl == 'NORP':
                    orgs.append(ent.text)
        return orgs

    def get_language(self):
        """
        Get product names

        :param doc: The document to parse
        :return:    A list of potential languages
        """
        langs = []
        if self.__document:
            for ent in self.__document.ents:
                lbl = ent.label_.upper()
                if lbl == 'LANGUAGE':
                    langs.append(ent.text)
        return langs

    def get_product(self):
        """
        Get product names

        :param doc: The document to parse
        :return:    A list of potential products
        """
        products = []
        if self.__document:
            for ent in self.__document.ents:
                lbl = ent.label_.upper()
                if lbl == 'PRODUCT':
                    products.append(ent.text)
        return products

    def parse_text(self, text):
        """
        Parse a text for named entities.

        :param text:    The text to parse
        :return:    Whether the document was parsed
        """
        self.__document = self.__nlp(text)
        return True
