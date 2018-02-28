# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.cache import cache
import pandas as pd
import jcml.settings as sets
import redis
import json

class myRedis:

    def __init__(self):
        pool = redis.ConnectionPool(host=str(sets.CACHES['default']['LOCATION']).split(':')[0],
                                    port=(int)(str(sets.CACHES['default']['LOCATION']).split(':')[1]), db=0)
        self.rd = redis.Redis(connection_pool=pool)

    #read cache user id
    def read_from_cache(self, key):
        value = self.rd.get(key)
        if value == None:
            data = None
        else:
            data = pd.read_msgpack(value)
        return data
    #write cache user id
    def write_to_cache(self, key,value):
        self.rd.set(key, value, sets.NEVER_REDIS_TIMEOUT)

    #self.write_to_cache("visitSet",visitSet)
    #visitSet =  self.read_from_cache("visitSet")

    def get_csv_cache(self,filePath):

        if self.rd.exists(filePath):
            fileCache = self.read_from_cache(filePath)
        else:
            fileCache = pd.read_csv(filePath)
            self.write_to_cache(filePath,fileCache.to_msgpack(compress='zlib'))
        return fileCache