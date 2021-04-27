
# @Title: 数值的整数次方 (数值的整数次方 LCOF)
# @Author: cocofe
# @Date: 2021-04-28 01:35:13
# @Runtime: 36 ms
# @Memory: 15.2 MB

class Solution:
    cache = {}
    def myPow(self, x: float, n: int) -> float:
        if (x, n) in self.cache:
            return self.cache[(x, n)]
        if n == 0:
            ret = 1
        elif n == 1:
            ret = x
        elif n == -1:
            ret = 1 / x
        elif n % 2 == 0:
            ret = self.myPow(x, n // 2) * self.myPow(x, n // 2)
        else:
            remain = n % 2
            ret = self.myPow(x, n // 2) * self.myPow(x, n // 2) * self.myPow(x, remain)
        self.cache[(x, n)] = ret
        return ret
