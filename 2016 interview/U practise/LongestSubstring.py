def lengthOfLongestSubstring(s):
    ans, start, end = 0, 0, 0
    hashmap = {}
    for c in s:
        end += 1
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1
        
        while hashmap[c] > 1:
            hashmap[s[start]] -= 1
            start += 1
        #print [start, end-1]
        ans = max(ans, end - start)
    return ans

if __name__ == "__main__":
    s = "abba"
    print lengthOfLongestSubstring(s)