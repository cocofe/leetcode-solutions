
# @Title: 股票的最大利润 (股票的最大利润  LCOF)
# @Author: cocofe
# @Date: 2020-09-21 20:54:07
# @Runtime: 20 ms
# @Memory: 13.4 MB

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = None
        length = len(prices)
        if length < 2:
            return 0
        cost = float('+inf')
        for i in range(2, length+1):
            # buy = min(prices[:i-1])  # 这个开销太大, 可以优化
            cost = min(cost, prices[i-2])
            sell = prices[i-1]
            ans = max(sell - cost, ans or 0 )
        return ans
