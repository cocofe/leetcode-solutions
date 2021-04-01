
# @Title: 不同的子序列 (Distinct Subsequences)
# @Author: cocofe
# @Date: 2021-03-17 01:55:03
# @Runtime: 36 ms
# @Memory: 16.1 MB

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1,len(t)+1):
            for j in range(1, len(s)+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[len(t)][len(s)]

        
            
