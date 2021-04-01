
# @Title: 4的幂 (Power of Four)
# @Author: cocofe
# @Date: 2020-08-16 21:27:30
# @Runtime: 16 ms
# @Memory: 12.7 MB

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return all([num ^ (4 ** i) for i in range(32)]) == 0
