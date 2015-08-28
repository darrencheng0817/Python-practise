#In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (e.g., each disk sits on top of an even larger one). You have the following constraints:
#(A) Only one disk can be moved at a time.
#(B) A disk is slid off the top of one rod onto the next rod.
#(C) A disk can only be placed on top of a larger disk.
#Write a program to move the disks from the first rod to the last using Stacks.


#first approach: recursion
#1), implement the Towers of Hanoi alg, 
#2), 1, source(disk - 1) to spare, 2, source(last) to destination 3, 3, spare(disk - 1) to destination

#reference
#http://www.cs.cmu.edu/~cburch/survey/recurse/hanoiimpl.html
#https://www.mathsisfun.com/games/towerofhanoi.html


#check each rod as a stack
Tower1 = [3, 2, 1]
Tower2 = []
Tower3 = []

def Move_item(T1, T2):
    item = T1.pop()
    T2.append(item)
    
    

def MoveTower(disk, source, spare, destination):
    if(disk <= 0):
        return
    else:
        MoveTower(disk-1, source, destination, spare)
        Move_item(source, destination)
        MoveTower(disk-1, spare, source, destination)
        
def run():
    global Tower1, Tower2, Tower3
    disk = 3
    MoveTower(disk, Tower1, Tower2, Tower3)
    

run()
print Tower1, Tower2, Tower3
        
        
        
    