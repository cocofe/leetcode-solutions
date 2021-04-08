
# @Title: 缺失的第一个正数 (First Missing Positive)
# @Author: cocofe
# @Date: 2021-04-07 23:51:32
# @Runtime: 44 ms
# @Memory: 14.9 MB

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [0] + nums
        length = len(nums)
        idx = 0
        while idx < length:
            num = nums[idx]
            while 1 <= num < length and num != idx:
                # 将idx对应的num放到num位置去
                nums[idx], nums[num] = nums[num], nums[idx]
                if nums[idx] == num:
                    break
                num = nums[idx]
            idx += 1
        for idx, num in enumerate(nums):
            if idx > 0 and idx != num:
                return idx
        return length
