# -*- coding: UTF-8 -*-
class Solution(object):
    """
    You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

    Example 1:
    coins = [1, 2, 5], amount = 11
    return 3 (11 = 5 + 5 + 1)
    
    Example 2:
    coins = [2], amount = 3
    return -1.
    
    Note:
    You may assume that you have an infinite number of each kind of coin.
    

    """
    def __init__(self):
        self.dp = {}

    def coinChange_TLE(self, coins, amount):
        """
        超时的解决方法
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount in coins:
            return 1
        if amount == 0:
            return 0
        if self.dp.get(amount):
            return self.dp[amount]
        imin = []
        for x in sorted(coins):
            if x < amount:
                count = self.coinChange_TLE(coins, amount - x)
                if count != -1:
                    imin.append(count + 1)
            else:
                break
        if not imin:
            self.dp[amount] = -1
        else:
            self.dp[amount] = min(imin)
        return self.dp[amount]

    def coinChange(self, coins, amount):
        """
        思路与上面超时的思路是一样的, 只是上面超时的解决方法使用递归实现的,而这个方法使用非递归实现的
        本质上本题类似于无限背包问题, 可以将此问题理解为在二叉树上寻找最短路径, 树的每一边表示coins的一种选取方式
        利用数组dp[i]来记录amount为i时的最小硬币数
        有如下动态方程
        dp[i] = 1 # if i in coins
        dp[i] = min(dp[i-x] + 1) for x in coins # x < i
        :param coins: 
        :param amount: 
        :return: 
        """
        dp = [0] * (amount + 1)
        coins = sorted(coins)
        imin = []
        for x in range(1, amount + 1):
            if x in coins:
                dp[x] = 1
            else:
                for c in coins:
                    if c < x and dp[x - c] != -1:
                        imin.append(dp[x - c] + 1)
                    elif c > x:
                        break
                if not imin:
                    dp[x] = -1
                else:
                    dp[x] = min(imin)
                    imin = []
        return dp[amount]

    def test(self):
        coins = [474,83,404,3]
        amount = 264
        print self.coinChange(coins, amount)




