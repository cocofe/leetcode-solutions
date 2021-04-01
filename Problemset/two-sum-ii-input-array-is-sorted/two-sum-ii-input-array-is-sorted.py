
# @Title: 两数之和 II - 输入有序数组 (Two Sum II - Input array is sorted)
# @Author: cocofe
# @Date: 2020-08-16 16:41:39
# @Runtime: 24 ms
# @Memory: 12.5 MB

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 二分查找, O(N*lgN)
        # def find(x, st, et):
        #     while st <= et:
        #         mid = (st + et) / 2
        #         if numbers[mid] > x:
        #             et = mid - 1
        #         elif numbers[mid] == x:
        #             return mid
        #         else:
        #             st = mid + 1
        # length = len(numbers)
        # for n, val in enumerate(numbers):
        #     et = find(target - val, n+1, length - 1)
        #     if et is None:
        #         continue
        #     return [n + 1, et + 1]
        # 双指针, O(N)
        start, end = 0, len(numbers) - 1
        while start < end:
            _sum = numbers[start] + numbers[end]
            if _sum == target:
                return [start + 1, end + 1]
            elif _sum < target:
                start += 1
            else:
                end -= 1
        


