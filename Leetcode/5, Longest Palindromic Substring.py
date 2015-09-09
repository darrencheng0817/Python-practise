#using the odd and even searching for longest palidrome sequence
#reference: http://stevekrenzel.com/articles/longest-palnidrome

class Solution(object):
    def longestPalindrome(self, s):
        """
            :type s: str
            :rtype: str
            """
        #two loops checking for both odd and even cases separately
        
        
        maxlength = 0
        result = ""
        #odd
        for i in range(0, len(s)):
            start, end = i, i
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    counter = end - start
                    if counter >= maxlength:
                        result = s[start : end+1]
                        maxlength = counter
                    start-=1
                    end+=1
                else:
                    break
        #even
        for i in range(0, len(s)-1):
            start, end = i, i+1
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    counter = end - start
                    if counter >= maxlength:
                        result = s[start : end+1]
                        maxlength = counter
                    start-=1
                    end+=1
                else:
                    break
        return result

print Solution().longestPalindrome('bb')