
# @Title: 判断子序列 (Is Subsequence)
# @Author: cocofe
# @Date: 2020-01-07 00:46:58
# @Runtime: 92 ms
# @Memory: N/A

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        is_sub = True
        p = 0
        if not s:
            return is_sub
        length = len(s)
        for _t in t:
            if _t == s[p]:
                p += 1
                if p >= length:
                    break
        return p == length
