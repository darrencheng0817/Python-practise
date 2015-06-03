#Implement a jigsaw puzzle. Design the data structures and explain an algorithm to solve the puzzle.
#[1,0,0,1]
#[0,0,0,0]
#[0,0,0,0]
#[1,0,0,1]

# ^------->|
# |        | ---------> logic
# |        |
# |        |
# <--------V


# my assumption: puzzle having piece having edges
global current_piece
global re_piece
global list1
class puzzle:
    def __init__ (self):
        global list1
        list1 = [[1,0,0,1],[0,0,0,0],[0,0,0,0],[1,0,0,1]]
        self.corner_piece = list1[0][0] + list1[0][3] + list1[3][0] + list1[3][3]
        self.other_piece = list1[0][1:3] + list1[1] + list1[2] +list1[3][1:3]
    
    #get a piece from the list(remaining piece)
    def get_value(self, type1):
        if type1 == "corner":
            re_piece = self.corner_piece.pop()
            return re_piece
        else:
            re_piece = self.other_piece.pop()
            return re_piece
            
    #direction of the edges         
    def check_edge(self, direction):
        for i in self.corner_piece:
            if i.edges[direction] == 0:
                current_piece = i
                return i.edges[direction]
        for i in self.other_piece:
            if i.edges[direction] == 0:
                current_piece = i
                return i.edges[direction]
    
    def remove_piece(self, item):
        if item in self.corner_piece:
            corner_piece.remove(item)
        elif item in self.other_piece:
            other_piece.remove(item)   
        
    
class piece:
    def __init__(self, postion):
        self.edges = position #[0, 0, 1, 0] set which edges can be used
    
   
    def check_opposite(self, direction):
        if direction == 1:
            if self.edge[4] == 0:
                self.edges[4] = 1
                return 4
            else:
                return None
        elif direction == 2:
            if self.edge[3] == 0:
                self.edges[3] = 1
                return 3
            else:
                return None
        elif direction == 3:
            if self.edge[2] == 0:
                self.edges[2] = 1
                return 2
            else:
                return None
        elif direction == 4:
            if self.edge[1] == 0:
                self.edges[1] = 1
                return 1
            else:
                return None
    def check_available(self):
        for i in range(0, len(self.edges)):
            if self.edges[i] == 0:
                self.edges[i] = 1
                return i
        else:
            return None
    
        
        
class edges:
    def __init__(self, index):
        self.index = index #1 -> up, 2 -> right, 3 -> left, 4 -> down
        self.attach = 0 #add the pieces togther based on puzzle
    
    def fitwith(self, item):
        pass
    
    def opposite(self):
        if self.index == 1:
            return 4
        elif self.index == 2:
            return 3
        elif self.index == 3:
            return 2
        elif self.index == 4:
            return 1
    def add_edges (self, edges):
        self.attach = edges
        
    
def get_exposed_edges(piece_1):
    #no more piece left
    if piece1 == None:
        return None
    edge = piece_1.check_available() 
    if edge != None:
        return edge
    else:
        return None
    
    
def main():
    puzzle1 = puzzle()
    #get the corner piece's edges
    current_edge = get_exposed_edges(puzzle1.get_value("corner"))
    while current_edge != None:
        opposite = edge.opposite()
        if edge.fitwith((puzzle1.check_edge(opposite))) == True:
            edges.add_edges(puzzle1.check_edge(opposite))
            #pop the current piece from puzzle 
            puzzle1.remove_piece(re_piece)
            #updating the current piece
            re_piece = current_piece
            #add the new check ---> updating new edges
            current_edge = current_piece.check_opposite()
            if current_edge == None:
                current_edge = current_piece.check_available()
            
    
   #we will start our loop from the corner
   

if __name__ == "__main__":
    main()
        