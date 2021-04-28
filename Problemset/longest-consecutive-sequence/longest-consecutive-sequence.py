
# @Title: 最长连续序列 (Longest Consecutive Sequence)
# @Author: cocofe
# @Date: 2021-04-28 23:14:59
# @Runtime: 48 ms
# @Memory: 16.1 MB

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        num_set = {num:True for num in nums}
        ans = 0
        for num in nums:
            cnt = 0
            if num - 1 in num_set:
                continue
            i = num
            while i in num_set:
                cnt += 1
                i += 1
            ans = max(cnt, ans)
        return ans
                

