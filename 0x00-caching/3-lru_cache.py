#!/usr/bin/env python3
''' This module contains the class LRUCache that inherits from the base class
BaseCaching. '''

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' Implements the put and get functions in accordance with
    LRU caching. '''

    def put(self, key, item):
        ''' Adds an item to the cache and removes the first (LRU position)
        item in the cache if there are more items than allowed. '''
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                key_list = list(self.cache_data)
                del_key = key_list[0]
                self.cache_data.pop(del_key)
                print("DISCARD:", del_key)

    def get(self, key):
        ''' Returns a value from the cache by the key and moves that key to
        the end (MRU position) of the dictionary. '''
        if key:
            item = self.cache_data.get(key)
            if item is not None:
                self.cache_data.pop(key)
                self.cache_data[key] = item
                return self.cache_data.get(key)
