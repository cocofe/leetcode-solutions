
# @Title: 旋转数组的最小数字 (旋转数组的最小数字  LCOF)
# @Author: cocofe
# @Date: 2021-04-09 22:50:50
# @Runtime: 36 ms
# @Memory: 15.2 MB

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers) - 1
        while left <= right:
            while left + 1 <= right and numbers[left] == numbers[left+1]:
                left += 1
            while right - 1 >= left and numbers[right] == numbers[right-1]:
                right -= 1
            mid = left + (right - left) // 2
            if numbers[left] <= numbers[mid]:
                if numbers[right] >= numbers[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 这个会不会造成死循环? --> 不会
                # 如果mid == right --> left == right, 则会导致死循环
                # 但是left == right 会在上面一个分支处理
                right = mid
        return numbers[left]
