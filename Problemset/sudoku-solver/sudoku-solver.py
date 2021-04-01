
# @Title: 解数独 (Sudoku Solver)
# @Author: cocofe
# @Date: 2020-11-08 23:03:12
# @Runtime: 852 ms
# @Memory: 13.3 MB

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def neighbor(_board, x, y):
            x = int(x)
            y = int(y)
            mapping = [(0, 2), (3, 5), (6, 8)]
            row, col = None, None
            for (start, end) in mapping:
                if row and col:
                    break
                if start <= x <= end:
                    row = (start, end)
                if start <= y <= end:
                    col = (start, end)
            used = set()
            
            for _row in range(row[0], row[1] + 1):
                for _col in range(col[0], col[1] + 1):
                    num = _board[_row][_col]
                    if num != '.':
                        used.add(str(num))
            for idx in range(9):
                num = _board[x][idx]
                num2 = _board[idx][y]
                for num in (_board[x][idx], _board[idx][y]):
                    if num != '.':
                        used.add(str(num))
            return used
        
        def find_next_space(_board, x, y):
            is_found = False
            x = int(x)
            y = int(y)
            while x != 8 or y != 8:
                y += 1
                if y // 9 == 1:
                    x += 1
                    y %= 9
                if _board[x][y] == '.':
                    is_found = True
                    break
            return None if not is_found else (str(x), str(y))
        ans = []
        def backtrack(_board, x, y, choices):
            if not choices:
                return
            for choice in choices:
                _board[int(x)][int(y)] = choice
                next_points = find_next_space(_board, x, y)
                if not next_points:
                    ans.append(copy.deepcopy(_board))
                    return
                used = neighbor(_board, next_points[0], next_points[1])
                _choices = [str(num) for num in range(1, 10) if str(num) not in used]
                backtrack(_board, next_points[0], next_points[1], _choices)
                _board[int(x)][int(y)] = '.'
        if board[0][0] == '.':
            next_points = 0, 0
        else:
            next_points = find_next_space(board, 0, 0)
            if next_points is None:
                return board
        used = neighbor(board, next_points[0], next_points[1]) 
        choices = [str(num) for num in range(1, 10) if str(num) not in used]
        backtrack(board, next_points[0], next_points[1], choices)
        for row_idx, rows in enumerate(ans[0]):
            for col_idx, col in enumerate(rows):
                board[row_idx][col_idx] = col
            

                    

