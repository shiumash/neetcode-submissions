class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        sort
        interate through list
        if num is same as num before skip (duplicate)
        two sum ii
        '''
        nums.sort()
        result = []

        for index, value in enumerate(nums):

            if value > 0:
                break

            if index > 0 and value == nums[index-1]:
                continue

            l, r = index + 1, len(nums) - 1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([value, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        
        return result