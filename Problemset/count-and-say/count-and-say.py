
# @Title: 外观数列 (Count and Say)
# @Author: cocofe
# @Date: 2020-01-07 01:33:09
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        dp = ['0', '1', '11', '21']
        if n < 4:
            return dp[n]
        for i in range(4, n+1):
            prev = dp[i-1]
            _cur, _nex = 0, 1
            length = len(prev)
            ret = ''
            same_count = 1
            while _nex < length:
                if prev[_cur] == prev[_nex]:
                    same_count += 1
                    _cur += 1
                    _nex += 1
                else:
                    ret += '{}{}'.format(same_count, prev[_cur])
                    same_count = 1
                    _cur = _nex
                    _nex = _cur + 1
            ret += '{}{}'.format(same_count, prev[_cur])
            dp.append(ret)
        return dp[n]
