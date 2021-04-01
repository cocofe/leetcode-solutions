
# @Title: 分割回文串 II (Palindrome Partitioning II)
# @Author: cocofe
# @Date: 2021-03-08 02:32:40
# @Runtime: 1980 ms
# @Memory: 234.1 MB

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_hw(string):
            return string == string[::-1]
        hw_map = {}
        for i in range(len(s)):
            for j in range(len(s)):
                hw_map.setdefault(i, {})
                hw_map[i][j] = is_hw(s[i:j+1])
        dp = collections.defaultdict(lambda: float('inf'))
        for i in range(len(s)):
            # 计算dp[i] (0~i的最小分割次数)
            if hw_map[0][i]:
                dp[i] = 0
                continue
            # 计算分割最近一个回文串x~i, 最小的分割次数
            for j in range(1, i+1):
                if not hw_map[j][i]:
                    continue
                dp[i] = min(dp[i], dp[j-1] + 1)
            
        return dp[len(s)-1]

                

