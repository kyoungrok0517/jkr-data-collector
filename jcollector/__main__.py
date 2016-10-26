# -*- coding: utf-8 -*-
"""The main entry point of data collector


"""
from __future__ import print_function, with_statement

import click
from pymongo import MongoClient

from jcollector.libs import get_logger
from jcollector.libs.config import ConfigLoader
from jcollector.twitter import TwitterCollector

# set logging
logger = get_logger(__file__)


# setup Config mechanism
class Config(object):
    """Config loader"""

    def __init__(self):
        self.twitter = ConfigLoader.get_twitter_config()
        self.mongo = ConfigLoader.get_mongo_config()

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
# @click.option('--home-directory', type=click.Path())
@pass_config
def main(config, verbose):
    """The entrypoint to jcollector

    Arguments:
        config (:obj:`Config`): global configs
        verbose (bool): verbose mode
    """
    config.verbose = verbose


@main.command()
def news(config):
    pass


@main.command()
@click.option('--limit', default=0, help='The number of documents to collect from each list.')
@click.option('--out', default='-', type=click.File('w'))
@click.option('--to-db', is_flag=True)
@pass_config
def twitter(config, limit, out, to_db):
    """Function that starts collecting tweets

    Arguments:
        limit (int): tweet count to collect
        out (click.File): output stream ('-' for stdout)
        to_db (bool): store to db or not

    Raises:
        ValueError
    """
    try:
        limit = int(limit)
    except ValueError:
        raise ValueError('limit must be integer!')

    # get the tweets
    client = MongoClient('mongodb://localhost:27017')
    db = client['jcollector']
    collection = db['tweets']
    collector = TwitterCollector(**config.twitter)
    for tweet in collector(limit=limit):
        if not to_db:
            click.echo(tweet, file=out)
        else:
            collection.insert(tweet)
