
# @Title: 排序数组 (Sort an Array)
# @Author: cocofe
# @Date: 2021-04-27 01:58:17
# @Runtime: 368 ms
# @Memory: 21.5 MB

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums):
            if not nums:
                return []
            p = random.choice(nums)
            left, mid, right = [], [], []
            for num in nums:
                if num < p:
                    left.append(num)
                elif num > p:
                    right.append(num)
                else:
                    mid.append(num)
            return quick_sort(left) + mid + quick_sort(right)
        return quick_sort(nums)
