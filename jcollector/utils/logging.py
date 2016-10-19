# -*- coding: utf-8 -*-
"""Logging-related utility functions

"""
import logging


def get_logger(name, logging_format='%(asctime)s %(levelname)-8s %(message)s', logging_level='WARNING'):
    """Get the logger with a given name

    Arguments:
        name (str): the logger name
        logging_format (str): the logging format
        logging_level (str): the logging level
    """
    logging.basicConfig(format=logging_format, level=logging_level)
    return logging.getLogger(name)