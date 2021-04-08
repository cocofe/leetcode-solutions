
# @Title: 斐波那契数列 (斐波那契数列  LCOF)
# @Author: cocofe
# @Date: 2021-04-09 01:17:46
# @Runtime: 40 ms
# @Memory: 14.8 MB

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        a, b = 0, 1
        for i in range(2, n+1):
            a, b = b, a + b
        return b % int(1e9+7)
        
