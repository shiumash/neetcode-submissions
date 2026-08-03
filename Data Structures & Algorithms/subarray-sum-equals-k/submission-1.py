class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        prefixsum = 0
        hashmap = {0: 1}
        for i in range(n):
            prefixsum += nums[i]
            diff = prefixsum - k
            count += hashmap.get(diff, 0)
            hashmap[prefixsum] = 1 + hashmap.get(prefixsum, 0)

        return count