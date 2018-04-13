# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example:
    
    Input: "babad"
    
    Output: "bab"
    
    Note: "aba" is also a valid answer.
     
    
    Example:
    
    Input: "cbbd"
    
    Output: "bb"
    """

    def longestPalindrome(self, s):
        """
        目的是求最长的子回文字符串, 所有的回文串一下两种情况, `aba`,`abba`, 即是:
         - 以单个字符为中心向两边扩散
         - 以两个相同的字符为中心向两边扩散
        因此可以逐一遍历字符串s(假设当前字符索引为idx),分别求以s[idx],和s[idx:idx+2]为中心所能的到回文串
        并取最大回文串
        :type s: str
        :rtype: str
        """
        ans = ''
        for x in range(len(s)):
            ans = max(ans, self.compute(s, x, x), self.compute(s, x, x + 1), key=len)
        return ans

    def compute(self, s, i, j):
        length = len(s)
        if j >= length:
            return s[i]
        while i >= 0 and j < length and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j]

    def test(self):
        s = 'cbbd'
        print self.longestPalindrome(s)
