import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        if len(nums) < 2:
            return nums[0]
        
        '''
        empty minheap arr
        for num in nums n
            heappush num -> minheap

            if length of minheap > k
                heappop minheap

        n * 2logk = nlogk 
        nlogk > nlogn (brute force)
        
        '''

        minheap = []
        for num in nums:
            heapq.heappush(minheap, num)

            if len(minheap) > k:
                heapq.heappop(minheap)

        return minheap[0]
        