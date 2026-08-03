class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        left right
        4 5 6 7 8^ 9 0 1 2 k =9
        5 6 7 0 1^ 1 1 2 4  k = 0
        if mid = target
            return mid
        if left <= mid
            left sorted arr
            if target > mid or target < left
                left = mid + 1
            if target < mid
                right = mid - 1
        if left > mid 
            right sorted arr
            if target > mid
                l= mid + 1
            if target < mid or (target > right)* go around
                r = mid - 1
        '''
        l, r = 0, len(nums) - 1
        if not nums:
            return -1
        

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                # left sorted arr
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                # right sorted arr
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                
        return -1