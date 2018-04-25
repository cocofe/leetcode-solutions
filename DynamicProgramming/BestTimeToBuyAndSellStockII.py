# -*- coding: UTF-8 -*-
class Solution(object):
    """
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
    
    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    
    Example 1:
    
    Input: [7,1,5,3,6,4]
    Output: 7
    Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                 Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
    Example 2:
    
    Input: [1,2,3,4,5]
    Output: 4
    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                 Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
                 engaging multiple transactions at the same time. You must sell before buying again.
    Example 3:
    
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
    """
    def maxProfit(self, prices):
        """
        本题解题关键是找出求最大利润的方法
        可以将价格波动想象成折线图, 则在波谷买入,在波峰卖出可以实现最大利润
        :type prices: List[int]
        :rtype: int
        """
        profit, idx = 0, 0
        length = len(prices)
        while idx < length:
            low = prices[idx]
            idx += 1
            while idx < length and prices[idx] < low:
                low = prices[idx]
                idx += 1
            height = low
            while idx < length and prices[idx] > height:
                height = prices[idx]
                idx += 1
            profit += height - low
        return profit

    def one_line_solve(self, prices):
        """
        Basically, if tomorrow’s price is higher than today’s, we buy it today and sell tomorrow. Otherwise, we don’t. Here is the code:
        :param prices: 
        :return: 
        """
        return sum(
            [max(prices[idx + 1] - prices[idx], 0) for idx in range(len(prices) - 1)])

    def test(self):
        prices = [7,1,5,3,6,4]
        print self.maxProfit(prices)
