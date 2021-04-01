
# @Title: 移除元素 (Remove Element)
# @Author: cocofe
# @Date: 2020-01-11 01:03:28
# @Runtime: 168 ms
# @Memory: N/A

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1 and nums[0] == val:
            return 0
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == val:
                offset = 1
                while i + offset < length and nums[i + offset] == val:
                    offset += 1
                tmp = i + offset
                replace_idx = i
                while tmp < length:
                    nums[replace_idx] = nums[tmp]
                    print nums, nums[0:length]
                    replace_idx += 1
                    tmp += 1
                length -= offset
            i += 1
        return length
