
# @Title: 岛屿的周长 (Island Perimeter)
# @Author: cocofe
# @Date: 2020-10-30 21:56:27
# @Runtime: 248 ms
# @Memory: 13.3 MB

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for row_idx, rows in enumerate(grid):
            for col_idx, col in enumerate(rows):
                if col == 0:
                    continue
                up = (row_idx - 1, col_idx) if row_idx - 1 >= 0 else None
                down = (row_idx + 1, col_idx) if row_idx + 1 < len(grid) else None
                left = (row_idx, col_idx - 1) if col_idx - 1 >= 0 else None
                right = (row_idx, col_idx + 1) if col_idx + 1 < len(rows) else None
                for idx, point in enumerate((up, down, left, right)):
                    if not point or grid[point[0]][point[1]] ==  0:
                        ans += 1
        return ans
                    

