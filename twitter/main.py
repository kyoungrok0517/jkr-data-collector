# -*- coding: utf-8 -*-
"""Collect tweets in my lists.

Todo:
    * cleaner code?
    * add testing
"""
from __future__ import print_function
import logging
import json
import time
import tweepy
from tweepy.error import TweepError

# set logging
LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
LOG_LEVEL = 'WARNING'
logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
logger = logging.getLogger(__file__)


class TwitterCollector(object):
    """Collect tweets with given API keys

    """

    def __init__(self, consumer_key, consumer_secret,
                 access_token, access_token_secret):
        # initiate tweepy API object
        self._api = self._init_api(consumer_key, consumer_secret,
                                   access_token, access_token_secret)

    def __call__(self, limit=0, *args, **kwargs):
        """Get the tweets from lists

        Arguments:
            limit (int): the number of tweets to get from each target list
            \*args: positional args
            \*\*kwargs: keyword args
        """
        # get tweets from my lists
        for l in self._api.lists_all():
            owner_screen_name = l.user.screen_name
            slug = l.slug

            try:
                for st in self._limit_handler(tweepy.Cursor(self._api.list_timeline,
                                                            owner_screen_name=owner_screen_name,
                                                            slug=slug).items(limit)):
                    ptw = self._process_tweet(st)
                    ptw['from_list'] = l.slug
                    yield json.dumps(ptw)
            except TweepError as e:
                logger.error(e)

    @staticmethod
    def _init_api(consumer_key, consumer_secret,
                  access_token, access_token_secret):
        # get oauth handler
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # set access token
        auth.set_access_token(access_token, access_token_secret)

        return tweepy.API(auth)

    @staticmethod
    def _limit_handler(cursor):
        while True:
            try:
                yield cursor.next()
            except tweepy.RateLimitError:
                time.sleep(15 * 60)

    @staticmethod
    def _process_tweet(st):
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
