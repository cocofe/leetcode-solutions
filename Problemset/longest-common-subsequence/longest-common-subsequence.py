
# @Title: 最长公共子序列 (Longest Common Subsequence)
# @Author: cocofe
# @Date: 2021-04-03 00:45:23
# @Runtime: 324 ms
# @Memory: 77.8 MB

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        for i, t1 in enumerate(text1):
            for j, t2 in enumerate(text2):
                if t1 == t2:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len(text1)-1][len(text2)-1]
