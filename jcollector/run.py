# -*- coding: utf-8 -*-
"""The main entry point of data collector


"""
from __future__ import print_function
from __future__ import with_statement
import click
from jcollector.twitter import TwitterCollector
from jcollector import settings
from jcollector.utils import get_logger

# set logging
logger = get_logger(__file__)


# setup Config mechanism
class Config(object):

    def __init__(self):
        self.verbose = False

        # Twitter
        self.twitter = dict()
        self.twitter['consumer_key'] = settings.TWITTER_CONSUMER_KEY
        self.twitter['consumer_secret'] = settings.TWITTER_CONSUMER_SECRET
        self.twitter['access_token'] = settings.TWITTER_ACCESS_TOKEN
        self.twitter['access_token_secret'] = settings.TWITTER_ACCESS_TOKEN_SECRET

pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
# @click.option('--home-directory', type=click.Path())
@pass_config
def cli(config, verbose):
    """The entrypoint to jcollector

    Arguments:
        config (:obj:`Config`): global configs
        verbose (bool): verbose mode
    """
    config.verbose = verbose


@cli.command()
def news(config):
    pass


@cli.command()
@click.option('--limit', default=0, help='The number of documents to collect from each list.')
@click.option('--out', default='-', type=click.File('w'))
@pass_config
def twitter(config, limit, out):
    # if config.verbose:
    #     click.echo('We are in verbose mode')

    # get the tweets
    collector = TwitterCollector(**config.twitter)
    for tw in collector(limit=limit):
        click.echo(tw, file=out)

