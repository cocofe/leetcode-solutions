# -*- coding: UTF-8 -*-
from collections import defaultdict


class Solution(object):
    """
    Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

    For example, given the following triangle
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
    
    Note:
    Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
    """
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

    def test(self):
        triangle = [[-1],[2,3],[1,-1,-3]]
        print self.minimumTotal(triangle)
