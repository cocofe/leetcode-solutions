
# @Title: 平方数之和 (Sum of Square Numbers)
# @Author: cocofe
# @Date: 2021-04-28 00:30:08
# @Runtime: 164 ms
# @Memory: 20.8 MB

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        nums = {i * i: True for i in range(1, int(c ** 0.5) + 1)}
        nums[0] = True
        for i in nums:
            if nums.get(c-i) or i == c:
                return True
        return False

