#round 1
#search an element in a rotated array, no duplicates
def find(list1, item):
    start = 0
    end = len(list1) -1
    
    #iteration
    while start <= end:
        mid = (start + end) / 2
        if list1[mid] == item:
            return mid
        elif list1[start] <= list1[mid]:
            if item >= list1[start] and item < list1[mid]:
                end = mid - 1
            else:
                start = mid +1
        elif list1[start] > list1[mid]:
            if item > list1[mid] and item <= list1[end]:
                start = mid + 1
            else:
                end = mid - 1
    return None
    
def main():
    list1 = [4, 5, 6, 1, 2, 3]
    item = 1
    print find(list1, item)
    
if __name__ == "__main__":
    main()
