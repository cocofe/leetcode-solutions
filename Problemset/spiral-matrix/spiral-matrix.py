
# @Title: 螺旋矩阵 (Spiral Matrix)
# @Author: cocofe
# @Date: 2021-03-15 00:36:14
# @Runtime: 8 ms
# @Memory: 13.1 MB

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        visited = set()
        ans = []
        direct = ['right', 'down', 'left', 'up']
        def helper(x, y, d_idx):
            if (x, y) in visited:
                return
            if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]):
                return
            if direct[d_idx] == 'right':
                while y < len(matrix[0]):
                    ans.append(matrix[x][y])
                    visited.add((x, y))
                    if (x, y+1) in visited:
                        return x + 1, y, d_idx + 1
                    y += 1
                return x + 1, y - 1, d_idx + 1
            elif direct[d_idx] == 'down':
                while x < len(matrix):
                    ans.append(matrix[x][y])
                    visited.add((x, y))
                    if (x + 1, y) in visited:
                        return x, y - 1, d_idx + 1
                    x += 1
                return x - 1, y - 1, d_idx + 1
            elif direct[d_idx] == 'left':
                while y >= 0:
                    ans.append(matrix[x][y])
                    visited.add((x, y))
                    if (x, y - 1) in visited:
                        return x - 1, y, d_idx + 1
                    y -= 1
                return x - 1, y + 1, d_idx + 1
            elif direct[d_idx] == 'up':
                while x >= 0:
                    ans.append(matrix[x][y])
                    visited.add((x, y))
                    if (x - 1, y) in visited:
                        return x, y + 1, (d_idx + 1) % 4
                    x -= 1
                return x + 1, y + 1, (d_idx + 1) % 4
            return
        i, j, k = 0, 0, 0
        while True:
            ret = helper(i, j, k)
            if ret is None:
                break
            i, j, k = ret
        return ans

            
