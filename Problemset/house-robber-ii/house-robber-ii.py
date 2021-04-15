
# @Title: 打家劫舍 II (House Robber II)
# @Author: cocofe
# @Date: 2021-04-15 23:55:17
# @Runtime: 40 ms
# @Memory: 14.7 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(start, end):
            pprev, prev = 0, 0
            for idx in range(start, end+1):
                num = nums[idx]
                curr = max(prev, pprev+num)
                pprev, prev = prev, curr
            return prev
        if len(nums) <= 2:
            return max(nums)
        return max(helper(0, len(nums)-2), helper(1, len(nums)-1))
            
