
# @Title: 新增的最少台阶数 (Add Minimum Number of Rungs)
# @Author: cocofe
# @Date: 2021-07-24 12:39:31
# @Runtime: 104 ms
# @Memory: 25 MB

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        curr_step = 0
        ans = 0
        for rung in rungs:
            diff = rung - curr_step
            ans += (diff - 1) // dist
            curr_step = rung
        return ans
            

