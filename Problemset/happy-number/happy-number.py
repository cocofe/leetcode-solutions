
# @Title: 快乐数 (Happy Number)
# @Author: cocofe
# @Date: 2021-04-27 00:42:26
# @Runtime: 28 ms
# @Memory: 14.9 MB

class Solution:
    def isHappy(self, n: int) -> bool:
        cache = {}
        def helper(num):
            if num in cache:
                return cache[num]
            ans = 0
            while num:
                remain = num % 10
                ans += remain ** 2
                num //= 10
            cache[num] = ans
            return ans
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = helper(n)
        return n == 1
