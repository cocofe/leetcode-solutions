
# @Title: 盛最多水的容器 (Container With Most Water)
# @Author: cocofe
# @Date: 2020-11-09 22:44:58
# @Runtime: 48 ms
# @Memory: 13.9 MB

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        """
        指针移动的策略:
        指针往里面移动的时候, 宽是减少的, 所以只有保证高度是增加的才有可能新面积大于已有的面积
        """
        ans = 0
        while left < right:
            # print left, right
            _sum = (right - left) * min(height[right], height[left])
            ans = max(ans, _sum)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans
