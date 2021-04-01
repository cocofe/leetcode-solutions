
# @Title: 宝石与石头 (Jewels and Stones)
# @Author: cocofe
# @Date: 2020-01-26 17:52:37
# @Runtime: 12 ms
# @Memory: N/A

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        for s in S:
            if s in J:
                count += 1
        return count
        
