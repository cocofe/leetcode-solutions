# -*- coding: UTF-8 -*-


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
                    replace_idx += 1
                    tmp += 1
                length -= offset
            i += 1
        return length

    def test(self):
        test_cases = [
            {
                'nums': [0, 1, 2, 2, 3, 0, 4, 2],
                'val': 0
            }
        ]
        for case in test_cases:
            self.removeElement(case['nums'], case['val'])
