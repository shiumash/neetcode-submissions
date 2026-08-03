class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        memo = {}
        def dfs(curSum, i):
            
            if i >= len(nums) or curSum > target:
                return False
            if curSum == target:
                return True
            if (curSum, i) in memo:
                return memo[(curSum, i)]

            result = dfs(curSum + nums[i], i+1) or dfs(curSum, i+1)
            memo[(curSum, i)] = result
            return result
        
        return dfs(0, 0)