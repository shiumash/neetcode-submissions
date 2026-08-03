class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''

        hashmap mapping charFreq to word(s) 

        iterate through every s in strs 
            create 26 long arr of 0
            for c in s
                increment the char index (0 is a, 1 is b, etc) by 1. use ord() asci
            
            hashmap immutable key is tuple version of count array, value is string


        return hashmap values
        '''
        mapping = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            mapping[tuple(count)].append(s)

        return list(mapping.values())