
# @Title: 寻找两个正序数组的中位数 (Median of Two Sorted Arrays)
# @Author: cocofe
# @Date: 2018-04-03 16:43:55
# @Runtime: 164 ms
# @Memory: N/A

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        if length == 1:
            return sum(nums1) + sum(nums2)
        if length % 2 == 0:
            fir, sec = length / 2 - 1, length / 2
        else:
            fir, sec = length / 2, length / 2

        count = 0
        lp, rp = 0, 0
        total = {}
        while lp < len(nums1) and rp < len(nums2):
            total[count] = min(nums1[lp], nums2[rp])
            if count == sec:
                return (total[fir] + total[sec]) / 2.0
            if nums1[lp] <= nums2[rp]:
                lp += 1
            else:
                rp += 1
            count += 1
        if lp < len(nums1):
            while lp < len(nums1):
                total[count] = nums1[lp]
                if count == sec:
                    return (total[fir] + total[sec]) / 2.0
                lp += 1
                count += 1
        elif rp < len(nums2):
            while rp < len(nums2):
                total[count] = nums2[rp]
                if count == sec:
                    return (total[fir] + total[sec]) / 2.0
                rp += 1
                count += 1
            
            
        
