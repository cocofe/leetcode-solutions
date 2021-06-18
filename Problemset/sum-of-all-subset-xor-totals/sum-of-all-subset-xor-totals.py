
# @Title: 找出所有子集的异或总和再求和 (Sum of All Subset XOR Totals)
# @Author: cocofe
# @Date: 2021-05-16 10:43:34
# @Runtime: 360 ms
# @Memory: 14.8 MB

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def get_xor(_nums):
            return reduce(lambda x,y:x ^ y, _nums)
        ans = 0
        def helper(sub_nums, length, idx):
            nonlocal ans
            if len(sub_nums) == length:
                ans += get_xor(sub_nums)
                return
            if idx >= len(nums):
                return
            for i in range(idx, len(nums)):
                sub_nums.append(nums[i])
                helper(sub_nums, length, i+1)
                sub_nums.pop()
        for length in range(1, len(nums)+1):
            # choice begin idx
            for idx, num in enumerate(nums):
                helper([num], length, idx+1)
        return ans
                

