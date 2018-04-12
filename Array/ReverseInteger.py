# -*- coding: UTF-8 -*-
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (x < 0)
        ret = s*int(str(s*x)[::-1])
        return ret if -2**31 < ret < 2**31-1 else 0

    def test(self):
        x = -123
        print self.reverse(x)
