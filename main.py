# -*- coding: utf-8 -*-
"""The main entry point of data collector


"""
from __future__ import print_function
from __future__ import with_statement
import click
import logging
import twitter_collector


# set logging
LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
LOG_LEVEL = 'INFO'
logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
logger = logging.getLogger(__file__)

# available commands
sources = 'twitter news'.split()


def main(*target_sources):
    if target_sources:
        # twitter
        if 'twitter' in target_sources:
            pass

        # news
        if 'news' in target_sources:
            pass

if __name__ == '__main__':
    pass
