#round 2 -> LRUCache

#I am using the OrderDictionary in python
#-> maintain a queue the ealiest time will be the end of the queue


# class collections.OrderedDict([items])
# Return an instance of a dict subclass, supporting the usual dict methods. An OrderedDict is a dict that remembers the order that keys were first inserted. If a new entry overwrites an existing entry, the original insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end.

# New in version 2.7.

# OrderedDict.popitem(last=True)
# The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.

from collections import OrderedDict

class LRUCache:
    #Defining the LRU cache -> capacity
    def __init__(self, capacity):
        self.capacity = capacity
        #remeber the order of the node insertion
        self.cache = OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            #refresh the order
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
    #set the value for certain key
    def set(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        #checking limit before a new insertion
        #if full, page eviction -> FIFO
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last = False)
        self.cache[key] = value

cache = LRUCache(3)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
print cache.cache
print cache.get(1)
print cache.cache
cache.set(4, 4)
print cache.get(2)
print cache.cache
