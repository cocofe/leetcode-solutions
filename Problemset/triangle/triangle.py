
# @Title: 三角形最小路径和 (Triangle)
# @Author: cocofe
# @Date: 2018-04-09 21:55:38
# @Runtime: 47 ms
# @Memory: N/A

from collections import defaultdict
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = defaultdict(lambda: defaultdict(int))
        for row_idx, row in enumerate(triangle):
            for col_idx, col_val in enumerate(row):
                if row_idx == 0:
                    dp[row_idx][col_idx] = col_val
                elif col_idx == 0:
                    dp[row_idx][col_idx] = dp[row_idx - 1][col_idx] + col_val
                elif col_idx == row_idx:
                    dp[row_idx][col_idx] = dp[row_idx - 1][col_idx - 1] + col_val
                else:
                    dp[row_idx][col_idx] = min(dp[row_idx - 1][col_idx],
                                               dp[row_idx - 1][col_idx - 1]) + col_val
        return min((dp[len(triangle) - 1]).values())
        
