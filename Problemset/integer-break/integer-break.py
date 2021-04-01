
# @Title: 整数拆分 (Integer Break)
# @Author: cocofe
# @Date: 2018-04-20 02:07:59
# @Runtime: 31 ms
# @Memory: N/A

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
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
            for x in range(1,5):
                dp[x] = x
        else:
            return (n // 2) * (n - n // 2) 
        for x in range(5, n+1):
            dp[x] = dp[3] * dp[x-3]
        return dp[n]
        
        
        
        
