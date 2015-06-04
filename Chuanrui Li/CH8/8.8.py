#Othello is played as follows: Each Othello piece is white on one side and black on the other. 
#When a piece is surrounded by its opponents on both the left and right sides, or both the top and bottom, it is said to be captured and its color is flipped. 
#On your turn, you must capture at least one of your opponent’s pieces. 
#The game ends when either user has no more valid moves, and the win is assigned to the person with the most pieces. 
#Implement the object oriented design for Othello.

global board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
class game:
    def __init__(self, id1, id2):
        self.player1 = id1
        self.player2 = id2

class player:
    def __init__(self, id, color):
        self.playerId = id
        self.playerColor = color #black is 1, white is 2
        self.count = 0

    def current_marks(self):
        counter = 0
        for element in self:
            for i in element:
                if i == 2:
                    counter++
        return counter

    def playing(self, coordinates):
        #set the playing chess color on the board
        board[coordinates[0]][coordinates[1]] = self.playerColor

        #change other chess color on the board
        def flip(self.playerColor, board):
            pass



