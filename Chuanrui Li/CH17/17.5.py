# The Game of Master Mind is played as follows:
# The computer has four slots containing balls that are red (R), yellow (Y), green (G) or blue (B). For example, the computer might have RGGB (e.g., Slot #1 is red, Slots #2 and #3 are green, Slot #4 is blue).
# You, the user, are trying to guess the solution. You might, for example, guess YRGB.
# When you guess the correct color for the correct slot, you get a “hit”. If you guess a color that exists but is in the wrong slot, you get a “pseudo-hit”. For example, the guess YRGB has 2 hits and one pseudo hit.
# For each guess, you are told the number of hits and pseudo-hits.
# Write a method that, given a guess and a solution, returns the number of hits and pseudo hits.

#example:
#RGGB -> YRGB: 2 hits, 1 pseudo hit
#RGBY -> GGRR: 1 hits, 1 pseudo hit

def checker(t1, g1):
  counter = 0
  list1 = []
  list2 = []
  #hits
  for i, j in zip(range(0, len(t1)), range(0, len(g1))):
    if t1[i] == g1[j]: 
      counter+=1
    else:
      list1 = list1 + [t1[i]]
      list2 = list2 + [g1[j]]
  print counter
  print list1, list2
  
  #pseudo hits
  counter2 = 0 
  for k in list1:
    if k in list2:
      counter2 += 1
  print counter2
    
  
  
  
def main():
  targeted = "RGBY"
  guess = "GGRR" #---> input
  checker(targeted, guess)

if __name__ == "__main__":
  main()







