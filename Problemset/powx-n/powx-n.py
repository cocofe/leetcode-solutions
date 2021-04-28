
# @Title: Pow(x, n) (Pow(x, n))
# @Author: cocofe
# @Date: 2021-04-28 23:02:52
# @Runtime: 44 ms
# @Memory: 14.8 MB

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
