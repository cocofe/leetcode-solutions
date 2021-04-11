
# @Title: 第 k 个数 (Get Kth Magic Number LCCI)
# @Author: cocofe
# @Date: 2021-04-11 15:31:29
# @Runtime: 44 ms
# @Memory: 14.8 MB

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        p3,p5,p7 = 0,0,0
        nums = [1]
        idx = 1
        while idx < k:
            num = min([nums[p3] * 3, nums[p5] * 5, nums[p7] * 7])
            if num == nums[p3] * 3:
                p3 += 1
            elif num == nums[p5] * 5:
                p5 += 1
            elif num == nums[p7] * 7:
                p7 += 1
            if num <= nums[-1]:
                continue
            nums.append(num)
            idx += 1
        return nums[-1]
