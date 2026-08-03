class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        resl = 0

        for i in range(len(s)):
            l, r = i, i
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    resl = l
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    resl = l
                l -= 1
                r += 1
        return s[resl:resl+resLen]