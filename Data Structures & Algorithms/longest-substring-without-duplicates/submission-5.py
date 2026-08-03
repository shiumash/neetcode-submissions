class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check, res = {}, 0
        l = 0
        for r in range(len(s)):
            if s[r] in check and check[s[r]] >= l:
                l = check[s[r]] + 1
            res = max(res, r-l+1)
            check[s[r]] = r
        return res

        '''
        value to index
        '''
