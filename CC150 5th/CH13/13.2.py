#Compare and contrast a hash table vs. an STL map. How is a hash table implemented? 
#If the number of inputs is small, what data structure options can be used instead of a hash table?

# Hash Table vs. STL map
Hash Table is implemented by the array of linked list. 
1, So the hash table will be a list of (key, value) pair
key1 -> value, value1, value2, ....
key2 -> value, value1, value2, ....
key3 -> value, value1, value2, ....

2, STL map is built by the BST. the search speed is logn is lower than the hashmap



