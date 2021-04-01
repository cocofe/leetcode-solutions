
# @Title: 最富有客户的资产总量 (Richest Customer Wealth)
# @Author: cocofe
# @Date: 2020-12-29 00:09:05
# @Runtime: 20 ms
# @Memory: 13.1 MB

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max([sum(moneys) for moneys in accounts])
