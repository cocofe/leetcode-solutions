
# @Title: 左旋转字符串 (左旋转字符串 LCOF)
# @Author: cocofe
# @Date: 2020-11-02 19:58:10
# @Runtime: 12 ms
# @Memory: 13.5 MB

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:]+s[:n]
