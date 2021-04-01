
# @Title: 一和零 (Ones and Zeroes)
# @Author: cocofe
# @Date: 2020-10-17 14:37:59
# @Runtime: 5464 ms
# @Memory: 14 MB

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        strs = sorted(strs, key=len)
        # print strs
        # 对于前i个字符串, 背包大小为m,n, 能拼出的最大数量
        # - 不拼装
        # - 拼装
        # dp[i][m][n] = max(max(dp[i-1][m-x][n-y]) + 1, dp[i][m][n])
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        for idx, s in enumerate(strs):
            need = collections.Counter(s)
            need.setdefault('0', 0)
            need.setdefault('1', 0)
            for _m in range(m+1, need['0']-1, -1):
                for _n in range(n+1, need['1']-1, -1):
                    dp[_m][_n] = max(dp[_m][_n], dp[_m-need['0']][_n-need['1']] + 1)
        return dp[m][n]
                    
