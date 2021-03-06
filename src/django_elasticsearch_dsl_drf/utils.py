"""
Utils.
"""

import datetime


__title__ = 'django_elasticsearch_dsl_drf.utils'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2017 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'DictionaryProxy',
    'EmptySearch',
)


class EmptySearch(object):
    """Empty Search."""

    def __init__(self, **kwargs):
        pass

    def __len__(self):
        return 0

    def __iter__(self):
        return iter([])


class DictionaryProxy(object):
    """Dictionary proxy."""

    def __init__(self, mapping):
        self.__mapping = mapping

    def __getattr__(self, item):
        val = self.__mapping.get(item, None)
        if isinstance(val, datetime.datetime):
            val = val.date()
        return val
