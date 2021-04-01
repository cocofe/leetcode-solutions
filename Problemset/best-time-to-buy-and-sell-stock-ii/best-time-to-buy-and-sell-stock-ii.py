
# @Title: 买卖股票的最佳时机 II (Best Time to Buy and Sell Stock II)
# @Author: cocofe
# @Date: 2020-11-08 19:40:17
# @Runtime: 40 ms
# @Memory: 14.1 MB

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([max(prices[idx+1] - prices[idx], 0) for idx in range(len(prices)-1)])
