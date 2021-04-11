
# @Title: 丑数 (Ugly Number)
# @Author: cocofe
# @Date: 2021-04-10 23:35:30
# @Runtime: 48 ms
# @Memory: 15 MB

class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        for i in (2, 3, 5):
            if n % i == 0:
                return self.isUgly(n // i)
        return False
        
