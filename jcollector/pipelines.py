"""Pipelines

"""
from jcollector.utils.config import ConfigLoader
from pymongo import MongoClient

class Pipeline(object):
    pass

class MongoPipeline(Pipeline):
    """MongoDB Pipeline"""
    def __init__(self):
        self.mongo_config = ConfigLoader.get_mongo_config()
        self.mongo_uri = MongoPipeline.get_uri_string(self.mongo_config)
        self.client = MongoClient(self.mongo_uri)

    def process(self, item, collection):
        """Insert passed item into DB

        Arguments:
            item (dict): the item to insert
            collection (str): the name of the collection to insert the given item
        """
        pass

    @staticmethod
    def get_uri_string(mongo_config):
        """Return Mongo URI string built from settings"""
        return 'mongodb://{user}:{password}@{url}:27017/{db}'.format(**mongo_config)
