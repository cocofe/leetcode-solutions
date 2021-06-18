
# @Title: 打家劫舍 II (House Robber II)
# @Author: cocofe
# @Date: 2018-04-10 16:49:35
# @Runtime: 33 ms
# @Memory: N/A

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = collections.defaultdict(int)
        ans = 0
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                if i - 2 != 0:
                    dp[i] = max(dp[i], dp[i-2] + num)
                if i - 3 != 0:
                    dp[i] = max(dp[i], dp[i-3] + num)
            else:
                dp[i] = max(dp[i-2], dp[i-3]) + num
            ans = max(dp[i], ans)
        return ans
