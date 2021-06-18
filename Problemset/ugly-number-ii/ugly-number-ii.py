
# @Title: 丑数 II (Ugly Number II)
# @Author: cocofe
# @Date: 2021-04-11 15:27:37
# @Runtime: 296 ms
# @Memory: 14.9 MB

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        nums = [1]
        idx = 1
        while idx < n:
            num = min([nums[p2] * 2, nums[p3] * 3, nums[p5] * 5])
            if num == nums[p2] * 2:
                p2 += 1
            elif num == nums[p3] * 3:
                p3 += 1
            elif num == nums[p5] * 5:
                p5 += 1
            # 5 * 3 == 3 * 5, 后续生成的最小值可能已经重复了, 应该跳过
            if num <= nums[-1]:
                continue
            nums.append(num)
            idx += 1
        return nums[-1]
       
        
