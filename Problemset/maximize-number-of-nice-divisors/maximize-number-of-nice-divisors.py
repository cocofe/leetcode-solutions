
# @Title: 好因子的最大数目 (Maximize Number of Nice Divisors)
# @Author: cocofe
# @Date: 2021-03-28 12:09:16
# @Runtime: 20 ms
# @Memory: 13.1 MB

class Solution(object):
    def maxNiceDivisors(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        if n<=4: return n
        if n==5: return 6
        if n==6: return 9
        if n==7: return 12
        q,r = divmod(n-4, 3)
        return pow(3, q, MOD) * self.maxNiceDivisors(r+4) % MOD
