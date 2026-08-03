class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def ways(k):
            if k in memo:
                return memo[k]
            if k == 1 or k == 0:
                return 1
            memo[k] = ways(k-1) + ways(k-2)
            return memo[k]
        
        return ways(n)
