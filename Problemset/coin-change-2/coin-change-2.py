
# @Title: 零钱兑换 II (Coin Change 2)
# @Author: cocofe
# @Date: 2020-10-23 00:19:31
# @Runtime: 148 ms
# @Memory: 13.2 MB

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # dp[i][j] 使用i位置的硬币能凑成金额为j的总数
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for _amount in range(1, amount + 1):
                if _amount - coin >= 0:
                    dp[_amount] += dp[_amount-coin]
        return dp[amount]
