"""Config-related helper functions

"""
from jcollector import settings

# setup Config mechanism
class ConfigLoader(object):
    """Config loader"""

    @staticmethod
    def get_twitter_config():
        """Returns twitter config object

            keys = ['consumer_key', 'consumer_secret', 'access_token', 'access_token_secret']

        Returns:
            twitter_config (obj):
        """
        twitter_config = dict()
        twitter_config['consumer_key'] = settings.TWITTER_CONSUMER_KEY
        twitter_config['consumer_secret'] = settings.TWITTER_CONSUMER_SECRET
        twitter_config['access_token'] = settings.TWITTER_ACCESS_TOKEN
        twitter_config['access_token_secret'] = settings.TWITTER_ACCESS_TOKEN_SECRET
        return twitter_config

    @staticmethod
    def get_mongo_config():
        """Returns mongo config object

            keys = ['host', 'port', 'user', 'password', 'db']

        Returns:
            mongo_config (obj):
        """
        mongo_config = dict()
        mongo_config['host'] = settings.MONGO_HOST
        mongo_config['port'] = settings.MONGO_PORT
        mongo_config['user'] = settings.MONGO_USER
        mongo_config['password'] = settings.MONGO_PASSWORD
        mongo_config['db'] = settings.MONGO_DB
        return mongo_config
