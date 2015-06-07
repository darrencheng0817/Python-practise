# Implement an algorithm to print all valid (e.g., properly opened and closed) combi- nations of n-pairs of parentheses.
# EXAMPLE:
# input: 3 (e.g., 3 pairs of parentheses)
# output: ()()(), ()(()), (())(), ((()))

#this is the result


def result(left, right, list1):
    #this is the wrong cases
    if left > right or left < 0:
        return
    elif left == 0 and right == 0:
        print list1
    else:
        
        result(left-1, right, list1 + "(") 
        result(left, right-1, list1 + ")") 

def main():
    count = 3
    list1 = [""]
    result(count, count, list1[0])
 
    

if __name__ == "__main__":
    main()



