
# @Title: 和可被 K 整除的子数组 (Subarray Sums Divisible by K)
# @Author: cocofe
# @Date: 2021-04-05 10:56:28
# @Runtime: 356 ms
# @Memory: 18.5 MB

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        pre_sum = 0
        cache = collections.defaultdict(int)
        cache[0] = 1
        ans = 0
        for num in A:
            pre_sum += num
            ans += cache[pre_sum % K]
            cache[pre_sum % K] += 1
        return ans
