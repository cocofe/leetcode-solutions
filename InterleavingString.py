# -*- coding: UTF-8 -*-
from collections import defaultdict


class Solution(object):
    """
    Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
    
    For example,
    Given:
    s1 = "aabcc",
    s2 = "dbbca",
    When s3 = "aadbbcbcac", return true.
    When s3 = "aadbbbaccc", return false.
    """

    def isInterleave(self, s1, s2, s3):
        """
        题目大意是判断可否依次(不改变顺序)利用s1和s2中元素组成s3
        首先判断三者长度是否匹配
        其次需要用到动态规划思想,比如需要一个a元素,且s1和s2中都可以取到, 
        但是只能从s2中取到才能得到正确结果,因此针对这种情况,可以有
        
        i表示s1中元素位置(从1开始计数),j表示s2中元素位置,dp[0][1]表示取s2第一个元素,
        如果s2[0] == s3[0]则值为True
         
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        dp = defaultdict(lambda: defaultdict(bool))
        len_1, len_2, len_3 = map(len, [s1, s2, s3])
        if len_1 + len_2 != len_3:
            return False
        for i in range(0, len_1 + 1):
            for j in range(0, len_2 + 1):
                if i == j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                        dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return dp[len(s1)][len(s2)]

    def test(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        print self.isInterleave(s1, s2, s3)