
# @Title: 到目标元素的最小距离 (Minimum Distance to the Target Element)
# @Author: cocofe
# @Date: 2021-05-02 12:07:31
# @Runtime: 36 ms
# @Memory: 15 MB

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = None
        for idx, num in enumerate(nums):
            if num == target:
                if ans is None:
                    ans = idx
                elif abs(idx - start) < abs(ans - start):
                    ans = idx
        return abs(ans - start)
