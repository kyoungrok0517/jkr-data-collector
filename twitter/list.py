# -*- coding: utf-8 -*-
"""Collect tweets in my lists.

Todo:
    * cleaner code?
    * add testing
"""
import logging
import time

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
        tw (Status): Tweepy Status instance

    Yields:
        dict: A dictionary that contains only necessary fields
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


def get_list_tweets(limit, target_lists):
    """A generator that yields tweets in my lists.

    Returns:
        tweets in my list
    """
    api = init_api()

    for list in api.lists_all():
        owner_screen_name = list.user.screen_name
        slug = list.slug

        try:
            for st in tweepy.Cursor(api.list_timeline,
                                    owner_screen_name=owner_screen_name,
                                    slug=slug).items(10):
                ptw = process_tweet(st)
                ptw['from_list'] = list.slug
                yield ptw
        except TweepError as e:
            logger.error(e)

if __name__ == '__main__':
    for tw in get_list_tweets():
        logger.info(tw)

