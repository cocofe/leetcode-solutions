
# @Title: 找不同 (Find the Difference)
# @Author: cocofe
# @Date: 2020-12-18 20:29:02
# @Runtime: 24 ms
# @Memory: 13.1 MB

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        for _s, count in c2.items():
            if c1.get(_s, 0) < count:
                return _s
