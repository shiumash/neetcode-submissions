class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1, 2, 4, 6
        
        1, 1, 2, 8 prefix
        48, 24, 6, 1 suffix

        48, 24, 12, 8

        multiply down

        '''

        n = len(nums)
        output = [1] * n
        prefix = 1
        postfix = 1

        if not nums or n < 2:
            return False

        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        for j in range(n-1, -1, -1):
            output[j] *= postfix
            postfix *= nums[j]

        return output


    

        
