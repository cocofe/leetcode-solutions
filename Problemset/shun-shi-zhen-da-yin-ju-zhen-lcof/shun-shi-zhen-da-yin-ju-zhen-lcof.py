
# @Title: 顺时针打印矩阵 (顺时针打印矩阵  LCOF)
# @Author: cocofe
# @Date: 2021-04-09 02:01:59
# @Runtime: 36 ms
# @Memory: 15.4 MB

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        vertex = 0
        ans = []
        if not matrix:
            return ans
        length = min(len(matrix), len(matrix[0]))
        while vertex * 2 < length:
            row, col = vertex, vertex
            end_col = len(matrix[0]) - vertex - 1
            end_row = len(matrix) - vertex - 1
            # right
            while col <= end_col:
                ans.append(matrix[row][col])
                col += 1
            col -= 1
            row += 1
            # down
            while row <= end_row:
                ans.append(matrix[row][col])
                row += 1
            row -= 1
            col -= 1
            # left
            while col >= vertex and end_row > vertex:
                # 不在同一行
                ans.append(matrix[row][col])
                col -= 1
            col += 1
            row -= 1
            # up
            while row > vertex and vertex < end_col:
                ans.append(matrix[row][col])
                row -= 1
            vertex += 1
        return ans


