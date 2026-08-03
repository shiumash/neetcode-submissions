class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        def dfs(curSum, i):
            
            if i >= len(nums) or curSum > target:
                return False
            if curSum == target:
                return True

            return dfs(curSum + nums[i], i+1) or dfs(curSum, i+1)
        
        return dfs(0, 0)