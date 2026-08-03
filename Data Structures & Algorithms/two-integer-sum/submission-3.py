class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in ref:
                return [ref[diff], index]
            ref[num] = index