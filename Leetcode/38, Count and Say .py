def find(string, num):
    if num == 1:
        return string
    
    outer = 0
    length = len(string)-1
    list1 = []
    #this is outer
    while outer < length:
        #print "hehe"
        #inner loop
        inner = outer
        counter = 1
        while string[inner] == string[inner+1]:
            counter += 1
            inner += 1
            if inner == length:
                break
        #store the data
        
        list1.extend([str(counter), str(string[inner])])
        #increment outer
        outer = outer + counter
    if inner < length:
        if string[inner] != string[inner+1]:
            list1.extend([str(1), str(string[inner+1])])

return find(''.join(list1), num-1)


class Solution(object):
    def countAndSay(self, n):
        """
            :type n: int
            :rtype: str
            """
        #read the string element one by one -> outer loop
        #add the counter for the duplicate -> inner loop
        #using a list to rececive the loop
        
        if n == 1:
            return '1'
        else:
        string = '11'
            return find(string, n-1)