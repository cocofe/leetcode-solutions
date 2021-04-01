
# @Title: 交错字符串 (Interleaving String)
# @Author: cocofe
# @Date: 2018-04-10 15:02:42
# @Runtime: 62 ms
# @Memory: N/A

from collections import defaultdict
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        dp = defaultdict(lambda: defaultdict(bool))
        len_1, len_2, len_3 = map(len, [s1, s2, s3])
        if len_1 + len_2 != len_3:
            return False
        for i in range(0, len_1+1):
            for j in range(0, len_2+1):
                if i == j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j-1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i-1] == s3[i + j - 1]
                else:
                    dp[i][j] = (dp[i][j - 1] and s2[j-1] == s3[i + j - 1]) or (
                    dp[i - 1][j] and s1[i-1] == s3[i + j - 1])
        return dp[len(s1)][len(s2)]
        
