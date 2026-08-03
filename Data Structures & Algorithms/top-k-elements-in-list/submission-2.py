class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap: freq, num
        # sort the keys by value / derive into a list of values sorted
        # while len res arr is less than k, get highest freq num

        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        arr = []
        arr = list(hashmap.items())
        arr.sort(key=lambda x: x[1])

        result = []
        while len(result) < k:
            result.append(arr.pop()[0])

        return result