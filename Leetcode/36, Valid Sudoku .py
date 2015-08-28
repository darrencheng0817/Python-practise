class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #check the rows and columns
        #check rows
        hashmap = {}
        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                if board[row][col] != '.':
                    #duplicates
                    if board[row][col] in hashmap:
                        return False
                    else:
                        hashmap[board[row][col]] = 1
                    #reset the hashmap
            hashmap = {}
        #check col   
        hashmap = {}
        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                if board[col][row] != '.':
                    #duplicates
                    if board[col][row] in hashmap:
                        return False
                    else:
                        hashmap[board[col][row]] = 1
                    #reset the hashmap
            hashmap = {}
            
        #check the 3*3 cell
        hashmap = {}
        num = len(board)/3
        for radd in range(0, num):
            for cadd in range(0, num):
                for row in range(0+3*radd, 3+3*radd):
                    for col in range(0+3*cadd, 3+3*cadd):
                        if board[row][col] != '.':
                            #duplicates
                            if board[row][col] in hashmap:
                                return False
                            else:
                                hashmap[board[row][col]] = 1
                            #reset the hashmap
                hashmap = {}
                
        return True