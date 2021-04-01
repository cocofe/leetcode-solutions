
# @Title: 直方图的水量 (Volume of Histogram LCCI)
# @Author: cocofe
# @Date: 2021-04-02 00:17:01
# @Runtime: 40 ms
# @Memory: 14.1 MB

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_max = [0]
        right_max = [0]
        for i in range(1, len(height)):
            left_max.append(max(left_max[-1], height[i-1]))
        for i in range(len(height)-2, -1, -1):
            right_max.append(max(right_max[-1], height[i+1]))
        right_max.reverse()
        # print left_max, right_max
        ans = 0
        for i in range(1, len(height)-1):
            ans += max(min(left_max[i], right_max[i]) - height[i], 0)
        return ans

