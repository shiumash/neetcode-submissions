class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')

            if amount in memo:
                return memo[amount]

            min_coins = float('inf')

            for coin in coins:
                result = dfs(amount - coin)
                if result != float('inf'):
                    min_coins = min(min_coins, result + 1)

            memo[amount] = min_coins
            return min_coins
        
        res = dfs(amount)
        return res if res != float('inf') else -1