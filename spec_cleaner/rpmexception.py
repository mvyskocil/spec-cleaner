# vim: set ts=4 sw=4 et: coding=UTF-8

import sys


class RpmBaseException(Exception):
    """
    Class wrapping Exception class so we throw neat exceptions.
    """

    def __init__(self, args=()):
        Exception.__init__(self)
        self.args = args

    def __str__(self):
        return ''.join(self.args)


class RpmWrongArgs(RpmBaseException):
    """
    Exception raised by wrong arguments pased by cli
    """


class RpmException(RpmBaseException):
    """
    Exception raised by wrong arguments pased by cli
    """
