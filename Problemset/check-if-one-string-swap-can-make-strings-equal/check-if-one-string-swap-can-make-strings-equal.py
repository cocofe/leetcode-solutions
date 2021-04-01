
# @Title: 仅执行一次字符串交换能否使两个字符串相等 (Check if One String Swap Can Make Strings Equal)
# @Author: cocofe
# @Date: 2021-03-14 12:14:54
# @Runtime: 20 ms
# @Memory: 13 MB

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        switch = None
        for i, j in zip(s1, s2):
            if i == j:
                continue
            if switch is None:
                switch = i
                continue
            if switch == j:
                switch = '-'
                continue
            return False
        if switch is not None and switch != '-':
            return False
        return True
