
# @Title: 有效三角形的个数 (Valid Triangle Number)
# @Author: cocofe
# @Date: 2021-04-28 02:37:12
# @Runtime: 1704 ms
# @Memory: 15 MB

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def binary_search(start, end, target):
            # 小于target的最右边界
            left, right = start, end
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1 if right > end or right < start else right
        cnt = 0
        nums.sort()
        for i in range(0, len(nums)-2):
            first = nums[i]
            if first == 0:
                continue
            for j in range(i+1, len(nums)-1):
                sec = nums[j]
                idx = binary_search(j+1, len(nums)-1, first + sec)
                if idx == -1:
                    continue
                cnt += idx - j
        return cnt
        
