
# @Title: 礼物的最大价值 (礼物的最大价值 LCOF)
# @Author: cocofe
# @Date: 2020-09-21 22:01:19
# @Runtime: 52 ms
# @Memory: 16 MB

class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = collections.defaultdict(dict)
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[row_idx])):
                left, up = 0, 0
                if col_idx - 1 >= 0:
                    left = dp[row_idx][col_idx-1]
                if row_idx - 1 >= 0:
                    up = dp[row_idx - 1][col_idx]
                dp[row_idx][col_idx] = max(up, left) + grid[row_idx][col_idx]
        return dp[len(grid)-1][len(grid[row_idx])-1]
