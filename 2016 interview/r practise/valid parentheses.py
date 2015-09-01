class Solution(object):
    def isValid(self, s):
        """
            :type s: str
            :rtype: bool
            """
        #iterate the list to store each element in the stack,
        #meanwhile, validate the pair,
        #if the pairs match, pop both from the stack
        #else, return false

        list1 = []
        #iteration
        for i in range(0, len(s)):
            if s[i] == '(' or  s[i] == '[' or s[i] == '{':
                list1.append(s[i])
            
            else:
                if len(list1) == 0: 
                    return False
                else:
                    result = list1.pop()
                    if self.check(result, s[i], list1) == False:
                        return False

        #final checking for an empty list
        if len(list1) == 0:
            return True
        else:
            return False
    
    def check(self, result, input1, list1):
        if (result == '(' and input1 == ')') or (result == '[' and input1 == ']') or (result == '{' and input1 == '}'):
            return True
        else:
            return False

    
    

print Solution().isValid("([])")