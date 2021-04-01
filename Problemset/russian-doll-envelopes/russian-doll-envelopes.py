
# @Title: 俄罗斯套娃信封问题 (Russian Doll Envelopes)
# @Author: cocofe
# @Date: 2021-03-05 01:01:52
# @Runtime: 6984 ms
# @Memory: 15 MB

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        # 宽度升序, 高度降序
        # 只需要基于高度, 求最长递增子序列
        # 为何高度要降序? 这样能保证, 相同宽度情况下, 高度只能选一个
        envelopes = sorted(envelopes, key=lambda arr: (arr[0], -arr[1]))
        hs = [h for w, h in envelopes]
        ans = 0
        dp = collections.defaultdict(lambda: 1)
        for i, h in enumerate(hs):
            for j in range(0, i):
                if hs[j] < h:
                    dp[i] = max(dp.get(i, 0), dp[j] + 1)
            ans = max(ans, dp[i])
        return ans
