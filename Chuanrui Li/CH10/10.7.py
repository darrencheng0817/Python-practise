#design a caching mechanism to cache the result of the most recent queries.
#Be sure to explain how you would update the cache when data changes.

# 1), LRU algorithm maintain a timestamp for each query result and update the timestamp for each read and write
# 2), the data structure is a hash table

Expend to many machine?

# 1), ans: each machine will hold a partial data of global cache: so for every query, the machine will go to 
# that computer to do the (query%N)  N is n computers

New page content related to a particular query, how to deal it?
#we need to have a time-out for the cache. each cache will be automatic updated after certain period.



