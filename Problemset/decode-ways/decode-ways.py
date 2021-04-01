
# @Title: 解码方法 (Decode Ways)
# @Author: cocofe
# @Date: 2020-09-21 23:23:24
# @Runtime: 24 ms
# @Memory: 12.8 MB

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 2 = 1
        # 22 = (2,2) + (22) = 2
        # 222 = (2,2,2), (22,2), (2, 22)
        # 2222 = (2,2,2,2), (22,2,2), (2, 22, 2), (2,2, 22), (22, 22)
        dp = {}
        for idx, val in enumerate(s):
            if idx == 0:
                if val == '0': 
                    return 0
                dp[idx] = 1
                continue
            prev = s[idx-1]
            if prev != '1' and prev != '2' and val == '0':
                return 0
            if int(prev + val) in (10, 20):
                dp[idx] = dp.get(idx-2, 1)
            elif 10 < int(prev + val) <= 26:
                dp[idx] = dp[idx-1] + dp.get(idx-2, 1)
            else:
                dp[idx] = dp[idx-1]
        return dp[len(s)-1]






