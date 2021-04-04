
# @Title: 搜索二维矩阵 II (Search a 2D Matrix II)
# @Author: cocofe
# @Date: 2021-04-04 23:59:18
# @Runtime: 184 ms
# @Memory: 20.9 MB

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 先定位列的范围
        # 比如查找10, 那么找到10最右可能边界(3)
        # 查找每列, 根据首尾判断是否在这一列
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[0][mid]
            if val == target:
                return True
            if val > target:
                right = mid - 1
            else:
                left = mid + 1
        for col in range(right, -1, -1):
            up, down = 0, len(matrix) - 1
            if matrix[down][col] == target:
                return True
            if matrix[down][col] < target:
                continue
            while up <= down:
                mid = up + (down - up) // 2
                if matrix[mid][col] == target:
                    return True
                if matrix[mid][col] > target:
                    down = mid - 1
                else:
                    up = mid + 1
        return False

            
