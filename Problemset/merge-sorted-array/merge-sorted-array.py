
# @Title: 合并两个有序数组 (Merge Sorted Array)
# @Author: cocofe
# @Date: 2021-04-05 00:20:09
# @Runtime: 32 ms
# @Memory: 14.6 MB

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2 = m - 1 , len(nums2) - 1
        n_right = len(nums1) - 1
        while n_right >= 0 and n2 >= 0:
            if n1 < 0:
                nums1[n_right] = nums2[n2]
                n_right -= 1
                n2 -= 1
                continue
            if nums1[n1] >= nums2[n2]:
                nums1[n_right] = nums1[n1]
                n_right -= 1
                n1 -= 1
            else:
                nums1[n_right] = nums2[n2]
                n2 -= 1
                n_right -= 1
