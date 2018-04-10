# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Follow up for "Unique Paths":

    Now consider if some obstacles are added to the grids. How many unique paths would there be?

    An obstacle and empty space is marked as 1 and 0 respectively in the grid.

    For example,
    There is one obstacle in the middle of a 3x3 grid as illustrated below.

    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    The total number of unique paths is 2.
    
    Note: m and n will be at most 100.


    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        width = len(obstacleGrid[0])
        d = [0] * width
        d[0] = 1
        for _, row in enumerate(obstacleGrid):
            for col_idx, col_val in enumerate(row):
                if col_val == 1:
                    # 通过该点的路的条数为0
                    d[col_idx] = 0
                else:
                    # 该点的路的条数 = top + left
                    if col_idx - 1 >= 0:
                        d[col_idx] += d[col_idx - 1]
        return d[width - 1]

    def test(self):
        t = [[0,0]]
        self.uniquePathsWithObstacles(t)