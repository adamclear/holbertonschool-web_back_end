#!/usr/bin/env python3
''' This module contains the class FIFOCache that inherits from the base class
BaseCaching. '''

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' Implements the put and get functions in accordance with FIFO caching. '''

    def put(self, key, item):
        ''' Adds an item to the cache and removes the oldest item in the
        cache if there are more items than allowed. '''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                key_list = list(self.cache_data)
                del_key = key_list[0]
                self.cache_data.pop(del_key)
                print("DISCARD:", del_key)

    def get(self, key):
        ''' Returns a value from the cache by the key. '''
        if key:
            return self.cache_data.get(key)
        else:
            return None
