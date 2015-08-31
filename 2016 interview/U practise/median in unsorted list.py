#round two
#find median in unsorted list -> quick select in the unsorted list

def quickSelect(list1, start, end, pos):
    mid = (start+end)/2
    
    #divide the list1 by Value of mid -> partition
    left = [item for item in list1 if item < list1[mid]]
    right = [item for item in list1 if item > list1[mid]]
    
    #the index of mid element in sorted order
    index = len(left)
    if index == pos:
        return list1[mid]
    #pos is within the left part of partition
    elif index > pos:
        return quickSelect(left, 0, len(left)-1, pos)
    elif index < pos:
        return quickSelect(right, 0, len(right)-1, pos - index-1)







def main():
    list1 = [4, 1, 7, 8, 2, 3, 9, 10]
    pos = len(list1)/2
    print quickSelect(list1, 0, len(list1)-1, pos)

if __name__ == "__main__":
    main()

