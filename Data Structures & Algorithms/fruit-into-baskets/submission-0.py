class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
         hashmap = defaultdict(int)
         l = 0
         total = 0
         res = 0
         
         for r in range(len(fruits)):
            hashmap[fruits[r]] += 1
            total += 1

            while len(hashmap) > 2:
                hashmap[fruits[l]] -= 1
                total -= 1
                if not hashmap[fruits[l]]:
                    hashmap.pop(fruits[l])
                l += 1
                

            res = max(res, total)

         return res
