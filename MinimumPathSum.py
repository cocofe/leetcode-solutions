# -*- coding: UTF-8 -*-
from collections import defaultdict


class Solution(object):
    """
    Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

    Note: You can only move either down or right at any point in time.
    
    Example 1:
    [[1,3,1],
     [1,5,1],
     [4,2,1]]
    Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.

    """

    def minPathSum(self, grid):
        """
        dp[i][j] 表示 i*j数组的最小路径和
        dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + val
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

    def test(self):
        grid = [[1,2],[1,1]]
        self.minPathSum(grid=grid)
