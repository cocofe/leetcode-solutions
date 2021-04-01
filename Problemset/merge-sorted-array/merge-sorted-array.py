
# @Title: 合并两个有序数组 (Merge Sorted Array)
# @Author: cocofe
# @Date: 2020-08-03 01:28:41
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return None
        len1 = len(nums1)
        tail1_idx = m - 1
        tail2_idx = n - 1
        tail = len1 - 1
        while tail2_idx >= 0 and tail1_idx >= 0:
            if nums2[tail2_idx] >= nums1[tail1_idx]:
                # move nums2
                nums1[tail] = nums2[tail2_idx]
                tail2_idx -= 1
            else:
                # move nums1
                tmp = nums1[tail1_idx]
                nums1[tail1_idx] = 0
                nums1[tail] = tmp
                tail1_idx -= 1
            tail -= 1
        while tail2_idx >= 0:
            nums1[tail] = nums2[tail2_idx]
            tail2_idx -= 1
            tail -= 1



