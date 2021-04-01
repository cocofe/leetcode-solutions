
# @Title: 单词搜索 (Word Search)
# @Author: cocofe
# @Date: 2021-03-08 03:02:08
# @Runtime: 9152 ms
# @Memory: 33.1 MB

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        col_len = len(board[0])
        row_len = len(board)
        ans = [False]
        visited = set()
        def dfs(x, y, w_idx, visited):
            if ans[0] or w_idx >= len(word):
                ans[0] = True
                return
            if (x >= col_len or x < 0 or y >= row_len or y < 0 or (x, y) in visited):
                return
            if board[y][x] != word[w_idx]:
                return
            w_idx += 1
            visited.add((x, y))
            dfs(x, y+1, w_idx, copy.copy(visited))
            dfs(x-1, y, w_idx, copy.copy(visited))
            dfs(x+1, y, w_idx, copy.copy(visited))
            dfs(x, y-1, w_idx, copy.copy(visited))
        for row_idx, row in enumerate(board):
            for col_idx, col in enumerate(row):
                if col == word[0]:
                    dfs(col_idx, row_idx, 0, set())
        return ans[0]
            
            
