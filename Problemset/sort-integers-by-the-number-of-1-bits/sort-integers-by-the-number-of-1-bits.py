
# @Title: 根据数字二进制下 1 的数目排序 (Sort Integers by The Number of 1 Bits)
# @Author: cocofe
# @Date: 2020-11-06 00:55:06
# @Runtime: 36 ms
# @Memory: 13.3 MB

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr2 = []
        for num in arr:
            _c = 0
            while num:
                if num & 0b1 == 0b1:
                    _c += 1
                num >>= 1
            arr2.append(_c)
        sorted_arr2 = sorted(list(set(arr2)))
        mapping = collections.defaultdict(list)
        for idx, num in enumerate(arr2):
            mapping[num].append(arr[idx])
        for num, arrs in mapping.items():
            mapping[num] = sorted(arrs)
        ans = []
        for num in sorted_arr2:
            ans.extend(mapping[num])
        return ans
        

