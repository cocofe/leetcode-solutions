# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
    
    For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
    
    Note: You may assume that n is not less than 2 and not larger than 58.
    """
    def integerBreak(self, n):
        """
        本题是要解决将一个大于1的正数拆成若干数求得其最大乘积, 主要是找到求最大乘积的规律
        实际上, 对于 n 在 2 ~ 4 之间 的数字, 其最大乘积小于等于自身的值, 当 n > 4, 其乘积大于本身
        而要获得最大值, 对于 n > 4, 可以 max = dp[3] * dp[n-3] 
        :type n: int
        :rtype: int
        """

        # 对于 n > 4 而言
        # n         dp[n]
        # 2 1       2
        # 3 1,2     3
        # 4 2,2     4
        # 5, 2,3    6
        # 6, 3,3    9
        # 7, 3,4    12
        # 8, 3,5    3*6=18
        # 9, 3,6    27
        # 10, 3,7   3*12=36
        # 11, 3,8   3*18=54
        # 12, 2,9   3*27=81
        # 15, 3,12

        dp = [0] * (n + 1)
        if n > 4:
            for x in range(1, 5):
                dp[x] = x
        else:
            return (n // 2) * (n - n // 2)
        for x in range(5, n + 1):
            dp[x] = dp[3] * dp[x - 3]
        return dp[n]



