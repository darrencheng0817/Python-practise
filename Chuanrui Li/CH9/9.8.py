# Given an infinite number of quarters (25 cents), dimes (10 cents), nickets(5 cents)
# and pennis(1 cents),
# Write code to calculate the number of ways of representing n cents?

number = 0

def ways(n, list1):
  print n
  global number
  if n < 0:
    return
  elif n == 0:
    i = 0
    increment = True
    while i+1 < len(list1):
      if list1[i+1] < list1[i]:
        increment = False
      i += 1
    if increment == True:  
      print list1
      number += 1
  else:
    ways(n-25, list1 + [25])
    ways(n-10, list1 + [10])
    ways(n-5, list1 + [5])
    ways(n-1, list1+ [1])


def main():
  global number
  #n is 10 cents
  n = 10
  curr = 25
  next = 25
  list1= []
  #counter 
  ways(n,list1)
  print "_____"
  print number

  
  

if __name__ == "__main__":
    main()












