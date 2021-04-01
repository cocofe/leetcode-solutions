
# @Title: 汉明距离 (Hamming Distance)
# @Author: cocofe
# @Date: 2020-04-11 02:08:02
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = x ^ y
        count = 0
        while ans > 0:
            if ans & 0b01 == 0b01:
                count += 1
            ans >>= 1
        return count
