
# @Title: Nim 游戏 (Nim Game)
# @Author: cocofe
# @Date: 2020-04-11 02:08:32
# @Runtime: 16 ms
# @Memory: N/A

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n < 4:
        #     return True
        # 4: 1, 3  false
        # 5: 1, 1, 3 win
        # 6: 2 1 3 win
        # 7: 3 1 3
        # 1, 3
        # 2, 2
        # 3, 1
        # 如果是4, 则必输
        # 1 win
        # 2 win
        # 3 win
        # 4 lose
        # 5: 1, 4 win
        # 6: 2, 4 win
        # 7: 3, 4 win
        # 8: 3, 5 false
        # 9, 10, 11 win
        # 12
        return n % 4 != 0
        
        
