#BS in sorted rotated array

#EXAMPLE:
#Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
#Output: 8 (the index of 5 in the array)

#-> two big cases
#the region is focused between [start, mid]

#-> case1: A[start] <= A[mid]
#(15 16 19 20 25 1 3 4 5 7 10 14)
#  |________|_..._|
# start    mid
    #-subcase: within the region[start, mid] -> sorted can define
    #           without the region[mid, end]

#-> case2: A[start] > A[mid]
#(15 16 19 20 25 1 3 4 5 7 10 14)
#            |___...____|______|
#           start      mid     end
    #-subcase: within the region[mid, end] -> sorted can define
    #           without the region[start, mid]



#diff from the 5th version, I will use iteration approach
def sorting(item, start, end, list1):
    
    while start <= end:
        
        mid = (start + end)/2
        #print start, end, mid
        if list1[mid] == item:
            return mid
        #case1
        elif list1[start] <= list1[mid]:
            #[start, mid]
            if list1[start] <= item and item < list1[mid]:
                end = mid - 1
            #[mid, end]
            else:
                start = mid + 1

        #case2
        elif list1[start] > list1[mid]:
            #[mid, end]
            if list1[mid] < item and item <= list1[end]:
                start = mid + 1
            #[start, mid]
            else:
                end = mid - 1
    return None



    

    
def main():
    element = 25
    list1 = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print sorting(element, 0, len(list1)-1, list1)
    

if __name__ == "__main__":
    main()
