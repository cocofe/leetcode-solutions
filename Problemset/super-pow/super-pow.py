
# @Title: 超级次方 (Super Pow)
# @Author: cocofe
# @Date: 2020-11-06 22:20:49
# @Runtime: 120 ms
# @Memory: 14 MB

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        def mypow(x, y):
            x %= 1337
            _sum = 1
            for _ in range(y):
                _sum *= x
                _sum %= 1337
            return _sum

        if not b: return 1
        end = b[-1]
        b.pop()
        part1 = mypow(a, end)
        part2 = mypow(self.superPow(a, b), 10)
        return part1 * part2 % 1337

