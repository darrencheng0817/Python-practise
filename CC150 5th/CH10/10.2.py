How would you design the data structures for a very large social network (Facebook, LinkedIn, etc)? 
Describe how you would design an algorithm to show the connection, or path, between two people (e.g., Me -> Bob -> Susan -> Jason -> You).


#structure for single node:
class Person { 
  Person[] friends; # Other info
}

#scalability -> Person info stored on different machines
Person[Machine_ID][Person_ID]


# Optimization: Reduce Machine Jumps
# Jumping from one machine to another is expensive. 
# Instead of randomly jumping from ma- chine to machine with each friend, try to batch these jumps—e.g., 
# if 5 of my friends live on one machine, I should look them up all at once.


# Optimization: Smart Division of People and Machines
# People are much more likely to be friends with people who live in the same country as them. 
# Rather than randomly dividing people up across machines, try to divvy them up by country, city, state, etc. 
# This will reduce the number of jumps.


# Usually, in BFS, we mark a node as visited by setting a flag visited in its node class. 
# Here, we don’t want to do that (there could be multiple searches going on at the same time,
# so it’s bad to just edit our data). In this case, we could mimic the marking of nodes with a hash table to lookup a node id a
# nd whether or not it’s been visited.