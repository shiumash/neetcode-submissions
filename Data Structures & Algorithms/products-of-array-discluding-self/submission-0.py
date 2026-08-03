class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1, 2, 4, 6
        
        1,  1,  2, 8 prefix
        48, 24, 6, 1 suffix

        multiply down

        '''
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res

    

        
