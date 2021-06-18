
# @Title: 零钱兑换 (Coin Change)
# @Author: cocofe
# @Date: 2021-04-21 02:13:45
# @Runtime: 1584 ms
# @Memory: 15.6 MB

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = collections.defaultdict(lambda:-1)
        for i in range(0, amount+1):
            if i == 0:
                dp[i] = 0
                continue
            ans = float('inf')
            for coin in coins:
                if coin > i:
                    continue
                prev = dp[i - coin] 
                if prev == -1:
                    continue
                ans = min(ans, prev + 1)
            if ans != float('inf'):
                dp[i] = ans
        return dp[amount]

                
        dp[i][j] = dp[i][j-1]
        ans = dp[amount][len(coins)-1]
        return -1 if ans == float('inf') else ans
