#Write a function that adds two numbers. 
#You should not use + or any arithmetic operators.


#There is an example->this is based 10
# 1. Add 759 + 674, but “forget” to carry. I then get 323.
# 2. Add 759 + 674 but only do the carrying, rather than the addition of each digit. I then get 1110.
# 3. Add the result of the first two operations 
#(recursively, using the same process de- scribed in step 1 and 2): 1110 + 323 = 1433.

#----- this is the first ------
#If I add two binary numbers together but forget to carry, bit[i] will be 0 if bit[i] in a and b are both 0 or both 1.
#This is an XOR.

#----- this is the second ------
#If I add two numbers together but only carry, I will have a 1 in bit[i] if bit[i-1] in a and b are both 1’s. 
#This is an AND, shifted.


def add(a, b):
  if b == 0:
    #1433 + 0 --> final round
    return a
  sumValue = a^b
  carry = (a & b) << 1 
  #1110 + 323 = 1433.--> second round
  
  return add(sumValue, carry)


def main():
 #759 + 674 --> first round
  x = add(2, 3)
  print x

  

if __name__ == "__main__":
  main()







