def lengthOfLongestSubstring(s):
    ans, start = 0, 0
    hashmap = {}
    for end in range(0, len(s)):
        #why start <= hashmap[s[end]]:
        #1, start < hashmap -> the index of hashmap only move forward,
        #if start > hashmap[s[end]], start will be reseted less than current start, backward move
        #if start == hashmap[s[end]], like 'bbbbb', start will still move forward by index 1
        
        if s[end] in hashmap and start <= hashmap[s[end]]:
            start = hashmap[s[end]] + 1
        #hashmap
        hashmap[s[end]] = end
        print [start, end]
        ans = max(ans, end - start + 1)
    return ans

if __name__ == "__main__":
    s = "abcabc"
    print lengthOfLongestSubstring(s)
