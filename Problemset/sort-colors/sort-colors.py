
# @Title: 颜色分类 (Sort Colors)
# @Author: cocofe
# @Date: 2021-04-29 00:23:07
# @Runtime: 28 ms
# @Memory: 14.8 MB

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        p0, p1 = 0, 0
        for idx, num in enumerate(nums):
            if num == 0:
                swap(p0, idx)
                if p0 == p1:
                    p1 += 1
                elif p0 < p1:
                    swap(idx, p1)
                    p1 += 1
                p0 += 1
            elif num == 1:
                swap(idx, p1)
                p1 += 1
        
            

