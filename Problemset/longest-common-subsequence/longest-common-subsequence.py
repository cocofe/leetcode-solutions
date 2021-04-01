
# @Title: 最长公共子序列 (Longest Common Subsequence)
# @Author: cocofe
# @Date: 2020-12-12 01:00:24
# @Runtime: 340 ms
# @Memory: 77.9 MB

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
