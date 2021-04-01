
# @Title: 两个数组的交集 (Intersection of Two Arrays)
# @Author: cocofe
# @Date: 2020-11-02 19:52:32
# @Runtime: 28 ms
# @Memory: 13.3 MB

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = map(set, [nums1, nums2])
        return nums2 & nums1
