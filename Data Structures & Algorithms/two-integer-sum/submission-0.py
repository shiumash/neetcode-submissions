class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}

        for index, val in enumerate(nums):
            complement = target - val
            if complement in ref:
                return [ref[complement], index]
            ref[val] = index
            
        return
