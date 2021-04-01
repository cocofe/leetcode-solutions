
# @Title: 硬币 (Coin LCCI)
# @Author: cocofe
# @Date: 2020-12-15 21:09:16
# @Runtime: 4872 ms
# @Memory: 395.5 MB

class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        coins = [1, 5, 10, 25]
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        for i in range(len(coins)):
            dp[0][i] = 1
        for i in range(1, n+1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i][j] = dp[i - coins[j]][j] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[n][len(coins)-1] % 1000000007



