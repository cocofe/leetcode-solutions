
# @Title: 统计「优美子数组」 (Count Number of Nice Subarrays)
# @Author: cocofe
# @Date: 2021-04-05 10:42:03
# @Runtime: 244 ms
# @Memory: 22.9 MB

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        cache = collections.defaultdict(int)
        ans = 0
        cache[0] = 1
        for num in nums:
            pre_sum += (1 if num % 2 != 0 else 0)
            ans += cache[pre_sum - k]
            cache[pre_sum] += 1
        return ans

