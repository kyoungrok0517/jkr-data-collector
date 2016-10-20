# -*- coding: utf-8 -*-
"""Defines item classes

"""
from collections import namedtuple

class Item(object):
    """Item"""

    def __init__(self, uids=None):
        """Init item

        you should set one or more field as uid
            ['field1', 'field2'] -> 'field1_field2' (uid)
        """
        if not uids:
            raise ValueError('You must set one or more UIDs!')
        if not (isinstance(uids, str) or isinstance(uids, list)):
            raise ValueError('uids must be string or list!')
        self._uids = uids

    def _get_uid_value(self):
        if isinstance(self._uids, str):
            return self._uids
        elif isinstance(self._uids, list):
            return '_'.join(self._uids)


class Tweet(Item):
    """Tweet

    Arguments:
        obj (obj): tweet object
        src (str): source of the tweet
    """
    __slots__ = [
        'id_str',
        'created_at',
        'entities',
        'favorite_count',
        'favorited',
        'lang',
        'retweet_count',
        'text',
        'coordinates',
        'src'  # custom field
    ]

    def __init__(self, obj, src):
        