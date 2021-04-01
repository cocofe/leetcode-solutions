
# @Title: 最小路径和 (Minimum Path Sum)
# @Author: cocofe
# @Date: 2018-04-09 17:18:44
# @Runtime: 65 ms
# @Memory: N/A

from collections import defaultdict


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        dp = defaultdict(lambda: defaultdict(int))
        dp[0][0] = grid[0][0]
        for row_idx, row_val in enumerate(grid):
            for col_idx, col_val in enumerate(row_val):
                if row_idx == 0 and col_idx == 0:
                    continue
                elif row_idx == 0:
                    dp[row_idx][col_idx] = dp[row_idx][col_idx - 1] + col_val
                elif col_idx == 0:
                    dp[row_idx][col_idx] = dp[row_idx-1][col_idx] + col_val
                else:
                    dp[row_idx][col_idx] = min(dp[row_idx - 1][col_idx],
                                               dp[row_idx][col_idx - 1]) + col_val
        return dp[len(grid) - 1][len(grid[0]) - 1]
