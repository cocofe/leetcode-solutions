
# @Title: 青蛙跳台阶问题 (青蛙跳台阶问题  LCOF)
# @Author: cocofe
# @Date: 2020-08-31 23:27:27
# @Runtime: 16 ms
# @Memory: 12.4 MB

class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for _ in range(n):
            # a 往后移一位
            a, b = b, a+b
        return a % 1000000007
