from flask import g
import os


def init(app):
    """ Function must be called to initalize this module """
    global _db_config


def _appinfocache_connect():
    """ Function must be called to initalize this module """

    try:

    except:
        pass

def get_appinfocache():
    appinfocache  = getattr(g, '_appinfocache', None)
    if appinfocache is None:
        appinfocache = g._appinfocache = _appinfocache_connect()
    return datastore

def close_connection(exception):
    appinfocache = getattr(g, '_appinfocache', None)
    if appinfocache is not None:
        print "xxx"