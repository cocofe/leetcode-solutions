
# @Title: 整数反转 (Reverse Integer)
# @Author: cocofe
# @Date: 2021-05-03 00:05:39
# @Runtime: 44 ms
# @Memory: 14.9 MB

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        ret = 0
        while x:
            ret = ret * 10 + x % 10
            x = x // 10
        return 0 if ret > 2 ** 31 - 1 else sign * ret
