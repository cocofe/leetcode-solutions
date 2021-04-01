
# @Title: 下一个更大元素 II (Next Greater Element II)
# @Author: cocofe
# @Date: 2021-03-06 00:16:02
# @Runtime: 188 ms
# @Memory: 14.8 MB

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums = nums * 2
        stack = []
        ans = []
        for i in new_nums[::-1]:
            while stack and stack[-1] <= i:
                stack.pop()
            ans.append(-1 if not stack else stack[-1])
            stack.append(i)
        ans.reverse()
        return ans[:len(nums)]
