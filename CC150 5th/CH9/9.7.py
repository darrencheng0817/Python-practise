# Implement the “paint fill” function that one might see on many image editing pro- grams. That is, 
# given a screen (represented by a 2 dimensional array of Colors), a point, and a new color, 
# fill in the surrounding area until you hit a border of that col- or.’



def fillup(x, y, list1):
  if x < 0 or y < 0 or x >= len(list1) or y >= len(list1):
    return
  #this condition prevent travel back and get infinite recursion
  elif list1[x][y] == 0:
    list1[x][y] = 1
    fillup(x-1, y, list1)
    fillup(x+1, y, list1)
    fillup(x, y-1, list1)
    fillup(x, y+1, list1)



def main():
  list1 = [ [ 0 for i in range(4) ] for j in range(4) ]
  x = 2
  y = 1
  fillup(x, y, list1)
  #fillup1(x, y, list1)
  print list1

if __name__ == "__main__":
    main()












