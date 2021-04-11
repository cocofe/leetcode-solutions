
# @Title: 找出游戏的获胜者 (Find the Winner of the Circular Game)
# @Author: cocofe
# @Date: 2021-04-11 11:10:00
# @Runtime: 36 ms
# @Memory: 14.7 MB

class Solution:
    def findTheWinner(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f + 1
        

