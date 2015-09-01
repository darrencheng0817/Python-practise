#round 1
#reverse word, do not reverse punctuation

import string


def reverse(str):
    list1 = []
    substr = ""
    word = ""
    index = 0
    while index < len(str):
        if str[index] not in set(string.punctuation):
            if len(substr) != 0:
                list1.append(substr)
                substr = ""
            word += str[index]
        else:
            if len(word) != 0:
                list1.append(word)
                word = ""
            substr += str[index]
        index += 1
    
    #add the last element
    if len(substr) != 0:
        list1.append(substr)
    else:
        list1.append(word)
    
    #reverse list
    start = 0
    end = len(list1) - 1
    while start < end:
        print start, end
        temp = list1[start]
        list1[start] = list1[end]
        list1[end] = temp
        #next pair
        start += 1
        end -= 1
        
        #skip the punctuation
        while list1[start][0] in set(string.punctuation):
            start += 1
        while list1[end][0] in set(string.punctuation):
            end -= 1


print list1




reverse('this,,,is.a word')