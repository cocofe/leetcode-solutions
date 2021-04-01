
# @Title: 零钱兑换 (Coin Change)
# @Author: cocofe
# @Date: 2020-12-16 00:33:18
# @Runtime: 2688 ms
# @Memory: 26.4 MB

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = collections.defaultdict(lambda: collections.defaultdict(lambda: float('inf')))
        for j in range(len(coins)):
            dp[0][j] = 0
        for i in range(1, amount+1):
            for j, coin in enumerate(coins):
                if i - coin == 0:
                    dp[i][j] = 1
                elif i - coin > 0:
                    dp[i][j] = min(1 + dp[i - coin][j], dp[i][j-1])
                else:
                    dp[i][j] = dp[i][j-1]
        ans = dp[amount][len(coins)-1]
        return -1 if ans == float('inf') else ans
