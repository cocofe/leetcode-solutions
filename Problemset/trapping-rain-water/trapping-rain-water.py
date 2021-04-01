
# @Title: 接雨水 (Trapping Rain Water)
# @Author: cocofe
# @Date: 2020-11-06 23:27:19
# @Runtime: 36 ms
# @Memory: 13.3 MB

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        idx = 0
        ans = 0
        left_max = []
        right_max = []
        _max = float('-inf')
        for h in height:
            _max = max(_max, h)
            left_max.append(_max)
        _max = float('-inf')
        for h in height[::-1]:
            _max = max(_max, h)
            right_max.append(_max)
        right_max = right_max[::-1]
        while idx < len(height) - 1:
            h = height[idx]
            r_max = right_max[idx]
            l_max = left_max[idx]
            if l_max > h and r_max > h:
                to_add = min(r_max, l_max) - h
                ans += to_add
            idx += 1
        return ans

