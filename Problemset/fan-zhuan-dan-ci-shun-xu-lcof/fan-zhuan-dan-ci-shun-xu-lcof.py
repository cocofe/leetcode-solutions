
# @Title: 翻转单词顺序 (翻转单词顺序 LCOF)
# @Author: cocofe
# @Date: 2020-08-31 23:33:58
# @Runtime: 16 ms
# @Memory: 13.5 MB

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([_s for _s in s.strip().split(' ') if _s][::-1])
