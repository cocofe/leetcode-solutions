
# @Title: 打印从1到最大的n位数 (打印从1到最大的n位数 LCOF)
# @Author: cocofe
# @Date: 2021-04-18 07:19:09
# @Runtime: 112 ms
# @Memory: 20.4 MB

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        ans = []
        def helper(nums, idx):
            nonlocal ans
            if idx == n:
                if nums:
                    s = ''.join(nums)
                    ans.append(int(s))
                return
            for i in range(10):
                if not nums and i == 0:
                    helper(nums[::], idx + 1)
                else:
                    nums.append(str(i))
                    helper(nums[::], idx + 1)
                    nums.pop()
        helper([], 0)
        return ans
        
