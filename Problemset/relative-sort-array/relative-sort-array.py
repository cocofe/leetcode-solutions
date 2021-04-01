
# @Title: 数组的相对排序 (Relative Sort Array)
# @Author: cocofe
# @Date: 2020-11-14 16:00:16
# @Runtime: 16 ms
# @Memory: 13.2 MB

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(arr1)
        ans = []
        for num in arr2:
            count = counter[num]
            ans.extend([num] * count)
            counter.pop(num)
        for num in sorted(counter.keys()):
            count = counter[num]
            ans.extend([num] * count)
        return ans
