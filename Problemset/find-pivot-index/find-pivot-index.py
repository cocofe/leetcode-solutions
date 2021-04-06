
# @Title: 寻找数组的中心下标 (Find Pivot Index)
# @Author: cocofe
# @Date: 2021-04-05 10:04:35
# @Runtime: 64 ms
# @Memory: 15.8 MB

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = []
        for num in nums:
            if not s:
                s.append(num)
            else:
                s.append(s[-1] + num)
        # print(s)
        for i in range(len(nums)):
            if i - 1 >= 0:
                left = s[i-1]
            else:
                left = 0
            if i + 1 < len(nums):
                right = s[-1] - s[i]
            else:
                right = 0
            if left == right:
                return i
        return -1


