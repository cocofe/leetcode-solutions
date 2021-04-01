
# @Title: 求1+2+…+n (求1+2+…+n LCOF)
# @Author: cocofe
# @Date: 2020-03-06 02:03:58
# @Runtime: 48 ms
# @Memory: 19 MB

class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n and (n + self.sumNums(n-1))
        
