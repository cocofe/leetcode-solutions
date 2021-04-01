
# @Title: 第一个只出现一次的字符 (第一个只出现一次的字符  LCOF)
# @Author: cocofe
# @Date: 2021-03-08 02:35:25
# @Runtime: 180 ms
# @Memory: 13.2 MB

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = collections.Counter(s)
        for i in s:
            if counter[i] == 1:
                return i
        return ' '
