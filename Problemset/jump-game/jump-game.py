
# @Title: 跳跃游戏 (Jump Game)
# @Author: cocofe
# @Date: 2021-04-03 01:22:36
# @Runtime: 32 ms
# @Memory: 14.3 MB

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        尽量跳的更远
        每次选择能跳的更远的台阶跳跃
        """
        farthest = 0
        for idx, step in enumerate(nums):
            farthest = max(farthest, idx + step)
            if idx >= farthest:
                break
        return farthest >= len(nums) - 1
        


