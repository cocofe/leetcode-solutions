
# @Title: 跳跃游戏 II (Jump Game II)
# @Author: cocofe
# @Date: 2021-04-03 01:36:33
# @Runtime: 16 ms
# @Memory: 13.3 MB

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step_end = 0
        farthest = 0
        jump_cnt = 0
        for idx, jump_step in enumerate(nums[:-1]):
            farthest = max(farthest, idx + jump_step)
            if idx == step_end:
                step_end = farthest
                jump_cnt += 1
        return jump_cnt

