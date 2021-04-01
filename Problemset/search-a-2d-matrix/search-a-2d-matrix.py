
# @Title: 搜索二维矩阵 (Search a 2D Matrix)
# @Author: cocofe
# @Date: 2021-03-30 01:54:10
# @Runtime: 20 ms
# @Memory: 13.1 MB

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) / 2
            x = mid / len(matrix[0])
            y = mid % len(matrix[0])
            # print left, right, x, y
            if target == matrix[x][y]:
                return True
            if target > matrix[x][y]:
                left = mid + 1
            else:
                right = mid - 1
        return False
