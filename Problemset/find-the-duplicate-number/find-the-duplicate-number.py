
# @Title: 寻找重复数 (Find the Duplicate Number)
# @Author: cocofe
# @Date: 2021-03-03 00:57:34
# @Runtime: 40 ms
# @Memory: 14.1 MB

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num <= mid + 1:
                    cnt += 1
            # [1,2,3,4,4] 长度为5的数组, 元素大小在1~4之间, 必然存在重复的元素
            # 对于数组中的某个值i, 对于小于等于i的元素个数cnt, 如果cnt > i, 则 在1~i这个区间必然存在重复元素, 
            # cnt == i, 则可能存在重复元素, 比如遍历到第一个4的时候, 4是重复数, 但是没法百分百确定, 当遍历到第二个4的时候就可以确定了
            if cnt <= mid + 1:
                left = mid + 1
            else:
                right = mid - 1
        return left + 1
