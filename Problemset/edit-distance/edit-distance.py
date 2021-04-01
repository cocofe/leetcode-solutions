
# @Title: 编辑距离 (Edit Distance)
# @Author: cocofe
# @Date: 2020-12-12 01:37:20
# @Runtime: 152 ms
# @Memory: 36.9 MB

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = {}
        # base case
        for i in range(len(word1)+1):
            dp[i] = {}
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i, w1 in enumerate(word1):
            for j, w2 in enumerate(word2):
                if w1 == w2:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j] + 1, dp[i+1][j] + 1, dp[i][j+1] + 1)
        return dp[len(word1)][len(word2)]

