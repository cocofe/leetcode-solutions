
# @Title: 摆动序列 (Wiggle Subsequence)
# @Author: cocofe
# @Date: 2021-04-23 02:44:12
# @Runtime: 44 ms
# @Memory: 15 MB

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        h, l = [1] + [0] * (len(nums) - 1), [1] + [0] * (len(nums) - 1)
        for i in range(1, len(nums)):
            num = nums[i]
            prev = nums[i-1]
            if num > prev:
                h[i] = max(h[i-1], l[i-1] + 1)
                l[i] = l[i-1]
            elif num < prev:
                l[i] = max(l[i-1], h[i-1] + 1)
                h[i] = h[i-1]
            else:
                l[i] = l[i-1]
                h[i] = h[i-1]
        return max([h[len(nums)-1], l[len(nums)-1]])
