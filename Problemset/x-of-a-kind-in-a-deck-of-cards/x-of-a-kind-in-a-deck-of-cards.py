
# @Title: 卡牌分组 (X of a Kind in a Deck of Cards)
# @Author: cocofe
# @Date: 2020-04-10 00:17:23
# @Runtime: 136 ms
# @Memory: N/A

from collections import Counter

def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if not deck or len(deck) < 2:
            return False
        x = list(set(Counter(deck).values()))
        return reduce(gcd, x) > 1
        
