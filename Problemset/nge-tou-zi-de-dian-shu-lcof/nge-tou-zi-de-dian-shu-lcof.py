
# @Title: n个骰子的点数 (n个骰子的点数  LCOF)
# @Author: cocofe
# @Date: 2020-08-11 01:18:25
# @Runtime: 280 ms
# @Memory: 12.4 MB

from collections import defaultdict
class Solution(object):
    def twoSum(self, n):
        """
        :type n: int
        :rtype: List[float]
        """
        dp = defaultdict(lambda: defaultdict(lambda: 0))
        for i in range(1, 7):
            dp[1][i] = 1
        for _n in range(2, n+1):
            for i in range(_n, _n * 6 + 1):
                dp[_n][i] = 0
                offset = 1
                while i - offset >= _n - 1 and offset < 7:
                    dp[_n][i] += dp[_n-1][i - offset]
                    offset += 1
                print dp
        return map(lambda v: float(v) / 6 ** n,  dp[n].values() )      

