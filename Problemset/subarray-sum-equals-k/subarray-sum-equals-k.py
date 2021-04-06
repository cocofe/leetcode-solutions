
# @Title: 和为K的子数组 (Subarray Sum Equals K)
# @Author: cocofe
# @Date: 2021-04-05 10:31:22
# @Runtime: 96 ms
# @Memory: 18.8 MB

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和
        pre_sum = 0
        ans = 0
        cache = collections.defaultdict(int)
        cache[0] = 1  # 表示 pre_sum == k的情况
        for num in nums:
            pre_sum += num
            ans += cache[pre_sum-k]
            cache[pre_sum] += 1
        return ans
