
# @Title: 数组元素积的符号 (Sign of the Product of an Array)
# @Author: cocofe
# @Date: 2021-04-11 10:34:22
# @Runtime: 36 ms
# @Memory: 15 MB

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        s = 1
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                s *= -1
        return s
                
