"""Pipelines

"""
from jcollector.libs.config import ConfigLoader
from jcollector.libs.logging import get_logger
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from abc import ABC
import logging

class Pipeline(ABC):
    pass

class MongoPipeline(Pipeline):
    """MongoDB Pipeline
    
    Arguments:
        config (obj):
            - host
            - port
            - user
            - password
            - db
    """
    def __init__(self, config, collector):
        self.config = config
        self.mongo_uri = self.get_uri_string()
        self.client = MongoClient(self.mongo_uri)
        # default db: jcollector
        self.db = self.client.jcollector
        self.logger = get_logger(name='mongo_pipeline')

    def process(self, item, collection):
        """Insert passed item into DB

        Arguments:
            item (dict): the item to insert
            collection (str): the name of the collection to insert the given item
        """
        doc = item.__dict__
        doc['_id'] = item.get_uid()

        # insert into given collection
        try:
            result = self.db[collection].insert_one(doc)
            self.logger.info(result.inserted_id)
        except DuplicateKeyError as e:
            self.logger.warning(e)

    def get_uri_string(self):
        """Return Mongo URI string built from settings"""
        config = self.config

        if config['user'] and config['password']:
            return 'mongodb://{user}:{password}@{host}:27017/{db}'.format(**config)
        else:
            return 'mongodb://{host}:27017/{db}'.format(**config)
