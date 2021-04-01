
# @Title: 岛屿数量 (Number of Islands)
# @Author: cocofe
# @Date: 2021-03-09 00:52:57
# @Runtime: 80 ms
# @Memory: 21.3 MB

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        ans = 0
        def dfs(row, col):
            if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
                return
            if (row, col) in visited:
                return
            if grid[row][col] == "1":
                visited.add((row, col))
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)
            else:
                return
        # 每次选择一个没遍历过得1开始遍历
        # 每次遍历都表示存在一个岛屿
        for r_idx, rows in enumerate(grid):
            for c_idx, col in enumerate(rows):
                if col == "1" and (r_idx, c_idx) not in visited:
                    dfs(r_idx, c_idx)
                    ans += 1
        return ans
