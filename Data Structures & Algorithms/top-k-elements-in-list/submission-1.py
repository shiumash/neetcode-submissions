class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        freq counter hash map
        create a list of n buckets, this list has the index being the freq and value being num
        in reverse order from end to beginning append items withinn each bucket up until the len of res arr is same as k
        '''

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res