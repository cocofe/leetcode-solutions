
# @Title: 回文子串 (Palindromic Substrings)
# @Author: cocofe
# @Date: 2020-12-29 00:28:51
# @Runtime: 268 ms
# @Memory: 58.9 MB

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = collections.defaultdict(lambda: collections.defaultdict(bool))
        for i in range(len(s)):
            dp[i][i] = True
        ans = len(s)
        i = len(s) - 1
        while i >= 0:
            for j in range(i+1, len(s)):
                if j - i != 1 and not dp[i+1][j-1]:
                    continue
                if s[i] == s[j]:
                    dp[i][j] = True
                if dp[i][j]:
                    ans += 1
            i -= 1
        # print dict(dp)
        return ans
        
