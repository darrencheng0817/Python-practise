#Given an input file with four billion integers, provide an algorithm to generate an integer which is not contained in the file. Assume you have 1 GB of memory.
#FOLLOW UP
#What if you have only 10 MB of memory?


#You can think this question as a page table design and memory management 
#There are 4 billion integers, we have 1GB memory
#1GB = 2^(30) byte = 2^(30) * 8 bit = 2^(33) bit = 8 billion bits

#We have 4 billion integers, based on this 1 bit represents 1 int
#All the bits will be initialized to "0"
#Everytime, there is an updating bits flip from 0 to 1
#Finally, check which bit is still 0 and report its index

#What if you have only 10 MB of memory?
#---> similar as two level page table design
#book ans:
#  memory size = 10MB = 2^3 MB = 2^23 bytes => # of int can be stored = 2^23 bytes / 4 bytes = 2^21 
# demo
# { 0 - 2^10: 2^10(int), 2^10 - 2^11: 2^10(int), ..... } => (Total size of the int) 2^31 / 2^21 = 2^10 -> each block size
# we do indicate the # of int within that range. if the value is equal to 2^10(int) - 1. Then we search that range
# using the same method as first question




