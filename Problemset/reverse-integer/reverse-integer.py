
# @Title: 整数反转 (Reverse Integer)
# @Author: cocofe
# @Date: 2018-04-06 18:54:27
# @Runtime: 56 ms
# @Memory: N/A

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = (x > 0) - (x < 0)
        ret = s*int(str(s*x)[::-1])
        return ret if -2**31 < ret < 2**31-1 else 0
        
            
        
