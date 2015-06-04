#Imagine a robot sitting on the upper left hand corner of an AxB grid. The robot can only move in two directions: right and down. 
#How many possible paths are there for the robot from (0,0) to (A, B)?

#FOLLOW UP
#Imagine certain squares are “off limits”, such that the robot can not step on them. Design an algorithm to get all possible paths for the robot.

  

#return method, sum up all the sub-solution to the top solution
#recursive relation:
#------------------ path(a,b) = path(a-1, b) + path(a, b-1)
 #0,1, 2
#0
#1
#2
def path(a, b):
    #base cases
    if a == 0 and b == 0:
        return 1
    if a < 0 or b < 0:
        return 0
    else:
        return path(a, b-1) + path(a-1, b)
    
def get_path(a, b, list1):
    if a == 0 and b == 0:
        list1.extend([(a,b)])
        return True
    if a < 0 or b < 0:
        return False
    if get_path(a, b-1, list1) or get_path(a-1, b, list1):
        list1.extend([(a,b)])
        return True
    return False

def main():
    A = 1
    B = 1
    print path(A, B)
    
    list1 = []
    get_path(A, B, list1)
    print list1

if __name__ == "__main__":
    main()








