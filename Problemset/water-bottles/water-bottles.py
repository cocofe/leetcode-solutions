
# @Title: 换酒问题 (Water Bottles)
# @Author: cocofe
# @Date: 2021-03-06 01:05:14
# @Runtime: 24 ms
# @Memory: 13.3 MB

class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans = [0]
        def helper(b, empty_bo):
            ans[0] += b
            to_exchange = (b + empty_bo) // numExchange
            left = (b + empty_bo) % numExchange
            if to_exchange == 0:
                return
            return helper(to_exchange, left)
        helper(numBottles, 0)
        return ans[0]

            
