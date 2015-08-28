#Given an integer, print the next smallest and next largest number that have the same number of 1 bits in their binary representation.

#1), question is want the next number with same number of 1 bits for both up counting and down counting
#2), the first approach is brute force, I will show the code here
#3), 1100011100 -> upper counting -> 
#----1100100000 -> First 0 flip to 1, Second put reset of number equals to 0 which is after "1"
#----1100100011 -> fill number of "1" at the end

#----1100100011 -> store the point as j
#----1100100000 -> clear all "1" after j and  #do the counting for NUM of "1"
#----1100011100 -> add all the 1 after j position


def nextbinary():
    list1 = [1, 1, 0, 0, 0, 0, 1, 1, 0, 1]
    list2 = [1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
    star = 0
    add_end = 0
    #find the "0" position and change the value
    #reverse access the list
    for i in range(len(list1)-1, -1, -1):
        if list1[i] == 1:
            while list1[i] == 1:
                i = i - 1
            #1000 case is not satisfied
            if i == -1:
                return 
            list1[i] = 1
            star = i
            break
    #print list1, star      
    #change the rest of value to be 0 and count the flips
    for i in range(len(list1)-1, -1, -1):
        if i == star:
            break
        if list1[i] == 1:
            list1[i] = 0
            add_end += 1
    #print list1, add_end            
    #add the flips amount of "1" to the end of the list
    for i in range(len(list1)-1, -1, -1):
        if add_end -1!= 0:
            list1[i] = 1
            add_end -= 1
        else:
            break
    print list1, add_end 

def prebinary():
    list1 = [1,1,0,0,1,0,0,0,1,1] 
    list2 = [0,0,0,1,1] 
    star = 0
    add_end = 0
    #store the point as j and flip list[i] 1 -> 0
    for i in range(len(list1)-1, -1, -1):
        if list1[i] == 0:
            while list1[i] == 0:
                i = i - 1
            #0001 case is not satisfied
            if i == -1:
                return             
            list1[i] = 0
            star = i
            break    
    print list1, star
    #clear all "1" after j and  #do the counting for NUM of "1"
    for i in range(len(list1)-1, -1, -1):
        if i == star:
            break
        if list1[i] == 1:
            list1[i] = 0
            add_end += 1    
    print list1, add_end
    
    #add all the 1 after j position
    start = star + add_end +1
    for i in range(start, -1, -1):
        if add_end +1!= 0:
            list1[i] = 1
            add_end -= 1
        else:
            break   
    print list1, add_end
    
#nextbinary()
prebinary()