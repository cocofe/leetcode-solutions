
# @Title: 下一个更大元素 I (Next Greater Element I)
# @Author: cocofe
# @Date: 2021-02-18 13:37:51
# @Runtime: 24 ms
# @Memory: 13.2 MB

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mapping_2 = {num:idx for idx, num in enumerate(nums2)}
        ans = []
        for num in nums1:
            idx = mapping_2[num]
            next_num = -1
            idx += 1
            while idx < len(nums2):
                if nums2[idx] > num:
                    next_num = nums2[idx]
                    break
                idx += 1
            ans.append(next_num)
        return ans
            

