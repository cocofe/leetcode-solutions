
# @Title: 颠倒二进制位 (Reverse Bits)
# @Author: cocofe
# @Date: 2021-03-29 02:18:35
# @Runtime: 16 ms
# @Memory: 12.9 MB

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        cnt = 32
        while cnt > 0:
            ans = ans | (n & 0b1)
            n >>= 1
            ans <<=1
            cnt -= 1
        return ans >> 1
