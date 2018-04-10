# -*- coding: UTF-8 -*-
from collections import defaultdict


class Solution(object):
    """
    Given a string S and a string T, count the number of distinct subsequences of S which equals T.

    A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
    
    Here is an example:
    S = "rabbbit", T = "rabbit"
    
    Return 3.
    """
    def numDistinct(self, s, t):
        """
        画出dp数组就可以找到规律了
        
              r  a  b  b  b  i  t
        
           1  1  1  1  1  1  1  1
        r  0  1  1  1  1  1  1  1
        
        a  0  0  1  1  1  1  1  1
                    +
        b  0  0  0  1= 2  3  3  3
                       + 
        b  0  0  0  0  1= 3  3  3
                          +
        i  0  0  0  0  0  0= 3  3
                             +
        t  0  0  0  0  0  0  0= 3
        
        
        
        i为s中元素位置,j为t中元素位置
        
        dp[i+1][j+1] = dp[i][j] + dp[i+1][j]  ; s[i] == s[j]
        dp[i+1][j+1] = dp[i+1][j] ; s[i] != s[j]  等于dp数组左边相邻元素的值
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = defaultdict(lambda: defaultdict(int))
        # init dp array
        for x in range(len(s) + 1):
            dp[0][x] = 1
        for i, i_val in enumerate(t):
            for j, j_val in enumerate(s):
                if i_val == j_val:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[len(t)][len(s)]









