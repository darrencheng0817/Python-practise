# You have a large text file containing words. 
# Given any two words, find the shortest distance (in terms of number of words) between them in the file. 
# Can you make the searching operation in O(1) time? 
# What about the space complexity for your solution?


#This problem can also be solved by hash table (key, location) ("hehe", [1, 2])
#but it requires more space, but more efficient
def minDistance(word1Pos, word2Pos, testFile):
  minD = len(testFile)
  Rword1 = "hehe"
  Rword2 = "jiji"
  for i in range(0, len(testFile)):
    if testFile[i] == Rword1:
      distance = abs(i - word2Pos)
      word1Pos = i
      if distance < minD:
        minD = distance

    elif testFile[i] == Rword2:
      distance = abs(word1Pos - i)
      word2Pos = i
      if distance < minD:
        minD = distance

  print minD
  
  
  
def main():
  testFile = ["hehe", "xixi", "yaya", "haha","jiji", "wuwu","hehe"]
  word1Pos = len(testFile)
  word2Pos = len(testFile)
  minDistance(word1Pos, word2Pos, testFile)

if __name__ == "__main__":
  main()







