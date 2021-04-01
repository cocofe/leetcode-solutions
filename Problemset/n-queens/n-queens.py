
# @Title: N 皇后 (N-Queens)
# @Author: cocofe
# @Date: 2020-09-22 21:48:22
# @Runtime: 56 ms
# @Memory: 12.9 MB

import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def get_invalid_cols(row, col, to_row):
            invalid_cols = [col]
            # down and left
            if col - (to_row - row) > 0:
                invalid_cols.append(col - (to_row - row))
            # down and right
            if col + (to_row - row) <= n:
                invalid_cols.append(col + (to_row - row))
            return invalid_cols
        ans = []
        def backtrace(path, row):
            if row > n:
                ans.append(path)
                return
            # 获取所有可选的路径
            invalid_cols = []
            for _row, _col in path.items():
                cols = get_invalid_cols(_row, _col, row)
                invalid_cols.extend(cols)
            valid_cols = [col for col in range(1, n+1) if col not in invalid_cols]
            if not valid_cols:
                return
            for col in valid_cols:
                origin_path = copy.copy(path)
                path[row] = col
                backtrace(path, row+1)
                path = origin_path
        backtrace({}, 1)
        format_ans = []
        for path in ans:
            _ans = []
            for row in range(1, n+1):
               col = path[row]
               _ans.append(''.join(['Q' if i+1 == col else '.' for i in range(n)]))
            format_ans.append(_ans)
        return format_ans
            
                
