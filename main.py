# -*- coding: utf-8 -*-
"""The main entry point of data collector


"""
from __future__ import print_function
from __future__ import with_statement
import click
import logging
import json
from twitter import TwitterCollector


# set logging
LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
LOG_LEVEL = 'WARNING'
logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
logger = logging.getLogger(__file__)


# setup Config mechanism
class Config(object):

    def __init__(self):
        self.verbose = False


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
    consumer_key = '1edbJ0RswuNVVfmhiXDz3tMtY'
    consumer_secret = 'MQleCAeXtNkCHU0P5LHFETPpySxK46bh4A25CxNT76aG6Uq2Hc'
    access_token = '17479200-o7Q1EEIXnsQnKlaPJuMlUbBThfLyUVp0sINi6668y'
    access_token_secret = 'zkrsRSJNRJwobouNTDRyre0dTrLvFJ4isWOyTepq0T2Rc'

    collector = TwitterCollector(consumer_key, consumer_secret, access_token, access_token_secret)
    for tw in collector(limit=limit):
        click.echo(tw, file=out)

