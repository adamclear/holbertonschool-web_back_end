#!/usr/bin/env python3
''' This module contains a class, BasicCache, that inherits from the base
class BaseCaching. '''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' Implements the put and get functions. '''

    def put(self, key, item):
        ''' Adds an item to the cache. '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        ''' Returns a value from the cache by the key. '''
        if key:
            return self.cache_data.get(key)
        else:
            return None
