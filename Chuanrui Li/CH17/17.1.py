#Write a function to swap a number in place without temporary variables.

# ############
# a = 2, b = 5
# b - a = 3

# ############
# a = 3, b = b-a = 2

# ############
# a = a+b = 5, b = 2

def more_type(a, b):
  a = a^b #xor find find the diff of two integers ---> a
  b = a^b #convert b to a, then assign # to b
  a = a^b #convert a to b, then assign # to a
  print a, b

def main():
  a = 2
  b = 10
  print a, b
  more_type(a, b)
  print a, b
  a = b-a #a=8
  b = b-a #b=2
  a = a+b #a=10
  print a, b

if __name__ == "__main__":
  main()







