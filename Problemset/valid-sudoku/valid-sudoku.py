
# @Title: 有效的数独 (Valid Sudoku)
# @Author: cocofe
# @Date: 2021-04-26 10:00:43
# @Runtime: 52 ms
# @Memory: 15 MB

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                box_idx = (r // 3) * 3 + (c // 3)
                if col == '.':
                    continue
                if col in cols[c]:
                    return False
                if col in rows[r]:
                    return False
                if col in boxes[box_idx]:
                    return False
                cols[c].add(col)
                rows[r].add(col)
                boxes[box_idx].add(col)
        return True
