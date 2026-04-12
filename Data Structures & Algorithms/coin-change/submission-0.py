class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [amount+1]*(amount+1)
        min_coins[0] = 0
        for num in range(amount+1):
            for c in coins:
                diff = num-c
                if diff >= 0:
                    min_coins[num] = min(min_coins[num], 1+min_coins[diff])
        return min_coins[amount] if min_coins[amount] != amount+1 else -1