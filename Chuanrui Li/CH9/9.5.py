#Write a method to compute all permutations of a string.
#level 1: c1
#level 2: c2c1, c1c2
#level 3: c2c1 -> [c3c2c1 c2c3c1 c2c1c3] c1c2 -> [c3c1c2, c1c3c2, c1c2c3]
from copy import deepcopy

list1 = []
def result(s1):
    global list1
    list1 = list1 + [s1[0]]
    #start at the second one
    i = 1
    #while i < len(s1):
        #new1 = s1[1] + list1[0]
        #new2 = list1[0] + s1[1]
        #list1 = list1 + [new1, new2]
        #i += 1

    # while i < len(s1):
    #     index = 0
    #     print "TTTTTTTTTTTTTTTTTTTTTTTT"
    #     while index < i:
    #         print "---------------"
    #         print index, i, list1[i-1], s1[i]
    #         slide = 0
    #         while slide <= i:
    #             snew4 = list1[i-1][0:slide] + s1[i] + list1[i-1][slide:]
    #             list1 = list1 + [snew4]
    #             slide += 1
    #         index += 1
    #     i += 1    
    while i < len(s1):
        index = 0
        #print "TTTTTTTTTTTTTTTTTTTTTTTT"
        result = []
        while index < len(list1):
            #print "---------------"
            #print index, i, list1[i-1], s1[i]
            slide = 0
            while slide <= i:
                #print list1
                #print i, index, slide
                snew4 = list1[index][0:slide] + s1[i] + list1[index][slide:]
                result = result + [snew4]
                slide += 1
            index += 1
        list1 = deepcopy(result)
        #print list1 
        i += 1   
        
        
def main():
    s1 = "abcef"
    result(s1)
    print list1
 
    

if __name__ == "__main__":
    main()






