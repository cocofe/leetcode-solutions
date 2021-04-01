
# @Title: 二进制中1的个数 (二进制中1的个数 LCOF)
# @Author: cocofe
# @Date: 2020-08-31 21:13:08
# @Runtime: 28 ms
# @Memory: 12.3 MB

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n > 0:
            if n & 1 == 1:
                ans += 1
            n >>= 1
        return ans
        
