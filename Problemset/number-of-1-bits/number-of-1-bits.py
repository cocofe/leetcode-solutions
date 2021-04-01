
# @Title: 位1的个数 (Number of 1 Bits)
# @Author: cocofe
# @Date: 2021-03-22 01:30:34
# @Runtime: 28 ms
# @Memory: 13.3 MB

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            if n & 0b1 == 0b1:
                ans += 1
            n >>= 1
        return ans

