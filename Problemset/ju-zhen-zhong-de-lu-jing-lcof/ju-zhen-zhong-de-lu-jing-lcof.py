
# @Title: 矩阵中的路径 (矩阵中的路径  LCOF)
# @Author: cocofe
# @Date: 2020-10-25 00:28:13
# @Runtime: 272 ms
# @Memory: 36.9 MB

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word: return True
        ans = [False]
        visited = set()
        row_len = len(board)
        col_len = len(board[0])
        def track(path, selected, visited):
            if ans[0]: return
            if not selected: return
            for x, y in selected:
                tmp = path[:]
                visited_tmp = visited.copy()
                path.append(board[x][y])
                if len(path) == len(word):
                    ans[0] = True
                    return
                elif len(path) > len(word):
                    return
                visited.add((x, y))
                selected = []
                up = (x - 1, y) if  x - 1 >= 0 else None
                down = (x + 1, y) if x + 1 < row_len else None
                left = (x, y - 1) if y - 1 >= 0 else None
                right = (x, y + 1) if y + 1 < col_len else None
                for point in (up, down, left, right):
                    # print path, selected, point, visited
                    if not point or point in visited or board[point[0]][point[1]] != word[len(path)]:
                        continue
                    selected.append(point)
                track(path, selected, visited)
                path = tmp
                visited = visited_tmp
        selected = []
        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                if col == word[0]:
                    selected.append((row_idx, col_idx))
        track([], selected, visited)
        return ans[0]
