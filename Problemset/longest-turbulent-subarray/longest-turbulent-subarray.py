
# @Title: 最长湍流子数组 (Longest Turbulent Subarray)
# @Author: cocofe
# @Date: 2021-04-27 01:53:24
# @Runtime: 128 ms
# @Memory: 18.3 MB

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up, down = [1] * len(arr), [1] * len(arr)
        ans = 0
        for i in range(1, len(arr)):
            num = arr[i]
            prev = arr[i-1]
            if num > prev:
                up[i] = down[i-1] + 1
                down[i] = 1
            elif num < prev:
                down[i] = up[i-1] + 1
                up[i] = 1
        return max(up + down)


