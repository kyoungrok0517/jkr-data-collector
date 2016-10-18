# -*- coding: utf-8 -*-
"""The main entry point of data collector


"""
import plac
import logging
import os
import json
from twitter.list import get_list_tweets

# set logging
LOG_FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
LOG_LEVEL = 'INFO'
logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)
logger = logging.getLogger(__file__)

@plac.annotations(
    target_lists=plac.Annotation('the target lists (every list if not specified)', 'option', 'l'),
    limit=plac.Annotation('The number of tweets to get from each target list', 'option', 'n', type=int),
    output_file=plac.Annotation('The output file path', 'option', 'o')
)
def twitter_list(target_lists=None, limit=10, output_file=None):
    """Get the tweets from lists

    Arguments:
        target_lists (list): the target lists (every list if not specified)
        limit (int): the number of tweets to get from each target list
        output_file (str): the output file path
    """
    if not target_lists:
        target_lists = []

    if output_file:
        if not os.path.exists(output_file):
            # prepare directories
            dirs = os.path.dirname(output_file)
            if not dirs == '.':
                os.makedirs(dirs)

            # output to file
            with open(output_file, 'w', encoding='utf-8') as fout:
                for tw in get_list_tweets(limit, target_lists):
                    fout.write(json.dumps(tw) + '\n')
        else:
            raise OSError('The output file already exists! Quitting the program...')
    else:
        for tw in get_list_tweets(limit, target_lists):
            logger.info(tw)

if __name__ == '__main__':
    # twitter list
    plac.call(twitter_list)

