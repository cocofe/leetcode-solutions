
# @Title: 螺旋矩阵 II (Spiral Matrix II)
# @Author: cocofe
# @Date: 2021-03-16 00:12:48
# @Runtime: 20 ms
# @Memory: 13.2 MB

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        array = [[0 for _ in range(n)] for _ in range(n)]
        visited = set()
        direct = ['right', 'down', 'left', 'up']
        point = [1]
        def helper(x, y, d_idx):
            if (x, y) in visited:
                return
            if x < 0 or y < 0 or x >= n or y >= n:
                return
            if direct[d_idx] == 'right':
                while y < n:
                    array[x][y] = point[0]
                    point[0] += 1
                    visited.add((x, y))
                    if (x, y+1) in visited:
                        return x + 1, y, d_idx + 1
                    y += 1
                return x + 1, y - 1, d_idx + 1
            elif direct[d_idx] == 'down':
                while x < n:
                    array[x][y] = point[0]
                    point[0] += 1
                    visited.add((x, y))
                    if (x + 1, y) in visited:
                        return x, y - 1, d_idx + 1
                    x += 1
                return x - 1, y - 1, d_idx + 1
            elif direct[d_idx] == 'left':
                while y >= 0:
                    array[x][y] = point[0]
                    point[0] += 1
                    visited.add((x, y))
                    if (x, y - 1) in visited:
                        return x - 1, y, d_idx + 1
                    y -= 1
                return x - 1, y + 1, d_idx + 1
            elif direct[d_idx] == 'up':
                while x >= 0:
                    array[x][y] = point[0]
                    point[0] += 1
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
        return array
