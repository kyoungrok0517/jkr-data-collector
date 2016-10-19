# -*- coding: utf-8 -*-
"""The main entry point of data collector


"""
from __future__ import print_function
from __future__ import with_statement
import click
import logging
import twitter


# setup Config mechanism
class Config(object):

    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)


# available commands
sources = 'twitter news'.split()


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
@click.argument('out', type=click.File('w'), default='-', required=False)
@pass_config
def twitter(config, limit, out):
    if config.verbose:
        click.echo('We are in verbose mode')


if __name__ == '__main__':
    pass
