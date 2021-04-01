
# @Title: 翻转字符串里的单词 (Reverse Words in a String)
# @Author: cocofe
# @Date: 2020-03-04 23:49:46
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        strings = s.split()
        strings.reverse()
        return ' '.join(strings)
            
