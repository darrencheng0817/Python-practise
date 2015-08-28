#Explain what the following code does: ((n & (n-1)) == 0).
#For example, n = 111001000 -> n-1 = 11000111 
#Inorder to satified the n & (n-1) == 0 bitwise
#except the first 1 counting from right hand side, other bits all need to be zero
# n = 000001000 -> n-1 = 000000111 => ((n & (n-1)) == 0).
# In this case, all the N should be power of 2 or (2^N)
