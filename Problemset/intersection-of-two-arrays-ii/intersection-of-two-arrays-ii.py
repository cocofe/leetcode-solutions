
# @Title: 两个数组的交集 II (Intersection of Two Arrays II)
# @Author: cocofe
# @Date: 2020-08-16 22:33:03
# @Runtime: 32 ms
# @Memory: 12.9 MB

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        # if len(nums1) < len(nums2):
        #     self.intersect(nums2, nums1)
        inner = set(nums1) & set(nums2)
        ans = []
        for i in inner:
            count = min(n1[i], n2[i])
            ans.extend([i] * count)
        return ans
