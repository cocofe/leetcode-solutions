
# @Title: 减小和重新排列数组后的最大元素 (Maximum Element After Decreasing and Rearranging)
# @Author: cocofe
# @Date: 2021-05-01 23:12:46
# @Runtime: 80 ms
# @Memory: 21.4 MB

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = None
        for num in arr:
            if not ans:
                ans = 1
            else:
                if num - ans <= 1:
                    ans = num
                else:
                    ans += 1
        return ans
        
