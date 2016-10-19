# -*- coding: utf-8 -*-
"""Collect tweets in my lists.

Todo:
    * cleaner code?
    * add testing
"""
from __future__ import print_function
from __future__ import with_statement
from io import open
import logging
import time
import plac
import os
import json

import tweepy
from tweepy.error import TweepError

# set logging
LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
LOG_LEVEL = 'INFO'
logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
logger = logging.getLogger(__file__)


def init_api():
    # consumer
    consumer_key = '1edbJ0RswuNVVfmhiXDz3tMtY'
    consumer_secret = 'MQleCAeXtNkCHU0P5LHFETPpySxK46bh4A25CxNT76aG6Uq2Hc'
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # access
    access_token = '17479200-o7Q1EEIXnsQnKlaPJuMlUbBThfLyUVp0sINi6668y'
    access_token_secret = 'zkrsRSJNRJwobouNTDRyre0dTrLvFJ4isWOyTepq0T2Rc'
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


def process_tweet(st):
    """Do the necessary

    Args:
        st (:obj:`Status`): `Tweepy` Status instance

    Yields:
        tw(:obj:`dict`): A dictionary that contains only necessary fields
    """
    fields = [
        'id_str',
        'created_at',
        'entities',
        'favorite_count',
        'favorited',
        'lang',
        'retweet_count',
        'text',
        'coordinates'
    ]
    st_obj = st._json
    return {sel_field: st_obj[sel_field] for sel_field in fields}


# @plac.annotations(
#     limit=plac.Annotation('The number of tweets to get from each target list', 'option', 'n', type=int),
#     output_file=plac.Annotation('The output file path', 'option', 'o')
# )
# def collect_list(limit=None, output_file=None):
#     """Get the tweets from lists
#
#     Arguments:
#         limit (int): the number of tweets to get from each target list
#         output_file (str): the output file path
#     """
#     api = init_api()
#
#     for l in api.lists_all():
#         # get the necessary information for querying tweets in the list
#         owner_screen_name = l.user.screen_name
#         slug = l.slug
#
#         try:
#             for st in tweepy.Cursor(api.list_timeline,
#                                     owner_screen_name=owner_screen_name,
#                                     slug=slug).items(limit):
#                 ptw = process_tweet(st)
#                 ptw['from_list'] = l.slug
#                 yield ptw
#         except TweepError as e:
#             logger.error(e)
#
#
# @plac.annotations(
#     target_lists=plac.Annotation('the target lists (every list if not specified)', 'option', 'l'),
#     limit=plac.Annotation('The number of tweets to get from each target list', 'option', 'n', type=int),
#     output_file=plac.Annotation('The output file path', 'option', 'o')
# )
# def twitter_list(target_lists=None, limit=10, output_file=None):
#     """Get the tweets from lists
#
#     Arguments:
#         target_lists (list): the target lists (every list if not specified)
#         limit (int): the number of tweets to get from each target list
#         output_file (str): the output file path
#     """
#     if not target_lists:
#         target_lists = []
#
#     if output_file:
#         if not os.path.exists(output_file):
#             # prepare directories
#             dirs = os.path.dirname(output_file)
#             if not dirs == '.':
#                 os.makedirs(dirs)
#
#             # output to file
#             with open(output_file, 'w', encoding='utf-8') as fout:
#                 for tw in get_list_tweets(limit, target_lists):
#                     fout.write(json.dumps(tw) + '\n')
#         else:
#             raise OSError('The output file already exists! Quitting the program...')
#     else:
#         for tw in get_list_tweets(limit, target_lists):
#             logger.info(tw)



@plac.annotations(
    lists=plac.Annotation(help='Collect lists', kind='flag'),
    favorites=plac.Annotation(help='Collect favorites', kind='flag')
)
def main(lists, favorites):
    pass
