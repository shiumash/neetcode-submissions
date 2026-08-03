from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return -1

        freq = Counter(nums)
        res = []
        counts = [[] for _ in range(len(nums) + 1)]
        for num, cnt in freq.items():
            counts[cnt].append(num)
        
        for i in range(len(counts) -1 , -1, -1):
            for num in counts[i]:
                res.append(num)
                if len(res) == k:
                    return res