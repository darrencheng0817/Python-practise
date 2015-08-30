#sorted list
#list1 is sorted array, k is the kth smallest element
def quickselect(list1, k):
    #midpoint of list1
    mid = len(list1)/2
    pivot = list1[mid]

    #bigger
    if k == mid:
        return pivot
    elif k > mid:
        return quickselect(list1[mid:], k-mid)
    elif k < mid:
        return quickselect(list1[:mid], k)
    
#unsorted
def quickselect1(list1, k):
    pivot = list1[len(list1)/2]
    
    #partition
    left = [item for item in list1 if item < pivot]
    right = [item for item in list1 if item > pivot]
    
    #index:
    mid = len(left)

    if k == mid:
        return pivot
    elif k < mid:
        return quickselect1(left, k)
    #need to exclude itself and less mid elements
    elif k > mid:
        return quickselect1(right, k-mid-1)
    


def main():      
    list1 = [1, 2, 3, 7, 9, 10]
    k = 4
    #print quickselect(list1, k)
    
    list2 = [7, 3, 4, 5, 10]
    print quickselect1(list2, k)
    
    
    

if __name__ == "__main__":
    main()


