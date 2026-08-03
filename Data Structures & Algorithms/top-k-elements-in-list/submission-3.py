class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap: freq, num
        # sort the keys by value / derive into a list of values sorted
        # while len res arr is less than k, get highest freq num
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():
            bucket[cnt].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res