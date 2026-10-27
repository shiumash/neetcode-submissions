class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = True
        for i in range(len(nums) - 1):
            if not nums[i + 1] >= nums[i]:
                increase = False
        if increase == True:
            return True
        
        for i in range(len(nums) - 1):
            if not nums[i + 1] <= nums[i]:
                increase = True
        if increase == False:
            return True
        
        return False
