
# @Title: 组合总和 Ⅳ (Combination Sum IV)
# @Author: cocofe
# @Date: 2021-04-24 10:23:13
# @Runtime: 48 ms
# @Memory: 14.9 MB

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = collections.defaultdict(int)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i - num < 0:
                    continue
                dp[i] += dp[i-num]
        return dp[target]
