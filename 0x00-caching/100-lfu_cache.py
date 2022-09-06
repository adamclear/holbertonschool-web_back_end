#!/usr/bin/env python3
''' This module contains the class LFUCache that inherits from the base class
BaseCaching. '''

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    ''' Implements the put and get functions in accordance with LFU caching. '''

    def __init__(self):
        ''' Initialization method.  '''
        super().__init__()
        self.NoU_dict = {}

    def put(self, key, item):
        ''' Adds an item to the cache and removes the LFU item in the cache 
        if there are more items than allowed. If items are tied for LFU, it
        goes by the LRU of those items. '''
        if key and item:
            if len(self.NoU_dict) > 0:
                del_key = self.find_LFU()
            self.cache_data[key] = item
            self.NoU_dict[key] = 1
            if len(self.cache_data) > self.MAX_ITEMS:
                self.cache_data.pop(del_key)
                self.NoU_dict.pop(del_key)
                print("DISCARD:", del_key)

    def get(self, key):
        ''' Returns a value from the cache by the key and moves that key to
        the end (MRU position) of the dictionary. Also adds 1 to the # of uses
        value in the NoU dictionary for that key. '''
        if key:
            item = self.cache_data.get(key)
            if item != None:
                self.cache_data.pop(key)
                self.cache_data[key] = item
                self.NoU_dict[key] += 1
                return self.cache_data.get(key)

    def find_LFU(self):
        ''' Returns the key to the LFU in cache. '''
        print(self.NoU_dict)
        LFU_value = min(self.NoU_dict.values())
        LFU_dict = {}
        for key, value in self.NoU_dict.items():
            if value == LFU_value:
                LFU_dict[key] = value
        print(LFU_dict)
        LFU_list = list(LFU_dict)
        print(LFU_list)
        return LFU_list[0]