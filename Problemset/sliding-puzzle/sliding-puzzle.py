
# @Title: 滑动谜题 (Sliding Puzzle)
# @Author: cocofe
# @Date: 2020-11-06 21:39:05
# @Runtime: 24 ms
# @Memory: 13 MB

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        neighbor = [
            [1,3],
            [0,2,4],
            [1,5],
            [0,4],
            [1,3,5],
            [2,4]
        ]
        target = list('123450')
        nums = board[0] + board[1]
        start = [str(num) for num in nums]
        if start == target: return 0
        q = collections.deque()
        q.append(start)
        step = 0
        visited = set()
        visited.add(''.join(start))
        while q:
            for _ in range(len(q)):
                s = q.popleft()
                zero_idx = s.index('0')
                neighbor_idxs = neighbor[zero_idx]
                for idx in neighbor_idxs:
                    s1 = s[:]
                    s1[zero_idx], s1[idx] = s1[idx], s1[zero_idx]
                    if ''.join(s1) in visited:
                        continue
                    if s1 == target:
                        return step + 1
                    q.append(s1)
                    visited.add(''.join(s1))
            step += 1
        return -1



