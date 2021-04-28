
# @Title: 青蛙过河 (Frog Jump)
# @Author: cocofe
# @Date: 2021-04-29 00:57:55
# @Runtime: 3104 ms
# @Memory: 24.2 MB

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        cache = {}
        def backtrack(idx, prev_step):
            if idx == len(stones) - 1:
                return True
            if (idx, prev_step) in cache:
                return cache[(idx, prev_step)]
            steps = [max(0, prev_step - 1), prev_step + 1]
            curr = stones[idx]
            ret = False
            for i in range(idx+1, len(stones)):
                stone = stones[i]
                if steps[0] <= stone - curr <= steps[1]:
                    ret = ret or backtrack(i, stone - curr)
            cache[(idx, prev_step)] = ret
            return ret
        return backtrack(0, 0)
