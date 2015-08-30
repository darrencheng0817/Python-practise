class Solution:
    # @return a boolean
    def isValid(self, s):
        #data structure: stack & hashmap
        stack, hashmap = [], {'(':')', '{':'}', '[':']'}
        for parenthess in s:
            if parenthess in hashmap:
                stack.append(parenthess)
            else:
                #two valid cases need to be checked
                if len(stack) == 0 or hashmap[stack.pop()] != parenthess:
                    return False

    return len(stack) == 0








if __name__ == "__main__":
    print Solution().isValid("()[]{}")
    print Solution().isValid("()[{]}")