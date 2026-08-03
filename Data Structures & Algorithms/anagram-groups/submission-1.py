from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list) #key: freq of each letter value: freq of the anagram
        for word in strs:
            count = [0] * 26
            for c in word: # a c t, 1, 3, 9
                count[ord(c) - ord('a')] += 1
            hashmap[tuple(count)].append(word)

        
        return list(hashmap.values())
