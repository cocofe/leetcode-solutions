
# @Title: 买卖股票的最佳时机 (Best Time to Buy and Sell Stock)
# @Author: cocofe
# @Date: 2018-04-20 03:05:32
# @Runtime: 52 ms
# @Memory: N/A

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profile, buy = 0, float('inf')
        for price in prices:
            buy = min(buy, price)
            profile = max(price - buy, profile)
        return profile

        
        
                
        
        
