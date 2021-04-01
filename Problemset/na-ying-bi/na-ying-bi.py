
# @Title: 拿硬币 (拿硬币)
# @Author: cocofe
# @Date: 2020-12-15 20:14:27
# @Runtime: 16 ms
# @Memory: 13.1 MB

class Solution(object):
    def minCount(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        count = 0
        for coin in coins:
            count += coin / 2
            if coin % 2 != 0:
                count += 1
        return count
