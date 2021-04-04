
# @Title: 截断句子 (Truncate Sentence)
# @Author: cocofe
# @Date: 2021-04-04 11:15:08
# @Runtime: 24 ms
# @Memory: 13 MB

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ss = s.split()
        return ' '.join(ss[:k])
