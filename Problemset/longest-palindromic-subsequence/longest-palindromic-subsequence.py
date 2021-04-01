
# @Title: 最长回文子序列 (Longest Palindromic Subsequence)
# @Author: cocofe
# @Date: 2020-12-14 22:24:10
# @Runtime: 1380 ms
# @Memory: 65.2 MB

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][len(s)-1]
                
                
