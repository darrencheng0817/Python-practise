list1 = []

def check(result, input1):
    global list1
    if input1 == '(' or  input1 == '[' or input1 == '{':
        list1.extend([result, input1])
        return True
    if (result == '(' and input1 == ')') or (result == '[' and input1 == ']') or (result == '{' and input1 == '}'):
        return True
    else:
        return False





def isValid(s):
    """
        :type s: str
        :rtype: bool
        """
    #iterate the list to store each element in the stack,
    #meanwhile, validate the pair,
    #if the pairs match, pop both from the stack
    #else, return false
    
    global list1
    
    #short cut for the invalid at the beginning input
    if s[0] ==')' or s[0] == '}' or s[0] == ']':
        return False
    else:
        list1.append(s[0])
    #iteration
    for i in range(1, len(s)):
        result = list1.pop()
        if check(result, s[i]) == False:
            return False
    
    #final checking for an empty list
    if len(list1) == 0:
        return True
    else:
        return False


print isValid("()")