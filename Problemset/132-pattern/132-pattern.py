
# @Title: 132 模式 (132 Pattern)
# @Author: cocofe
# @Date: 2021-03-25 09:23:19
# @Runtime: 40 ms
# @Memory: 14.1 MB

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        # 维护一个左侧最小序列, left_min(idx) 值为idx左侧最小的元素
        left_min = [nums[0]]
        for idx in range(1, len(nums)):
            left_min.append(min(left_min[idx-1], nums[idx-1]))
        # 利用单调递减栈, 从尾部开始遍历, 遍历idx位置元素, left_min为左侧最小值
        # 弹出栈中比左侧最小值还要小的元素, 如果栈不为空, 且 当前的值 > 栈顶 > left_min则存在132模式
        stack = []
        for idx in range(len(nums)-1, 0, -1):
            left_min_val = left_min[idx]
            curr = nums[idx]
            while stack:
                if stack[-1] <= left_min_val:
                    stack.pop()
                else:
                    break
            if stack and curr > stack[-1] > left_min_val:
                return True
            stack.append(curr)
        return False

