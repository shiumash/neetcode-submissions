class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        left and right pointer and 0, 1
        right pointer at duplicate 
        if slice left {} right == right + 1 : right-left
        ''' 
        l, res = 0, 0
        charSet = set()
        
        for n in range(len(s)):

            while s[n] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[n])
            res = max(res, n-l+1)
        return res