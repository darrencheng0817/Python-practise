#We have the following method used in a chess game: boolean canMoveTo(int x, int y) x and y are the coordinates of the chess board and 
#it returns whether or not the piece can move to that position. 
#Explain how you would test this method.


Checking whether input is within the board limit.
» Attempt to pass in negative numbers
» Attempt to pass in x which is larger than the width
» Attempt to pass in y which is larger than the width
Depending on the implementation, these should either return false or throw an exception.


- for each chess, check 4 different directions to go and the same check for directions
Do the same checking for all the chess again