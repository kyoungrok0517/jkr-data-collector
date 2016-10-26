"""Abstract classes for collector
"""
from abc import ABC
from abc import abstractmethod

class Collector(ABC):
    """Abstract class for Collector

    """
    @abstractmethod
    def stop(self, uid, msg):
        """Stop the collector

        Arguments:
            uid (str): the uid of the item that invoked stop signal
            msg (str): stop message
        """
        raise NotImplementedError(msg)


class Item(ABC):
    """Abstract class for Item

    """
    @abstractmethod
    def get_uid(self):
        """Get the unique id of this item using its one or more field values

        Returns:
            uid (str): the unique id
        """
        raise NotImplementedError
