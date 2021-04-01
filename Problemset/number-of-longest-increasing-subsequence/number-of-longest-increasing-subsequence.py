
# @Title: 最长递增子序列的个数 (Number of Longest Increasing Subsequence)
# @Author: cocofe
# @Date: 2020-12-27 03:00:25
# @Runtime: 1232 ms
# @Memory: 13.8 MB

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = collections.defaultdict(lambda: (1,1))
        max_length = 1
        ans = 0
        for i, num in enumerate(nums):
            j = i - 1
            choices = []
            while j >= 0:
                if nums[j] < num:
                    choices.append(j)
                j -= 1
            if choices:
                c = [dp[j][0] + 1 for j in choices]
                _length = max(c)
                _count = sum([dp[j][1] for j in choices if dp[j][0] == _length - 1])
                dp[i] = (_length, _count)
                if _length > max_length:
                    ans = _count
                    max_length = _length
                elif _length == max_length:
                    ans += _count
            else:
                if max_length == 1:
                    ans += 1
        return ans
