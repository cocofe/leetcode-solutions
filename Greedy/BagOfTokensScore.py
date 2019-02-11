# -*- coding: UTF-8 -*-

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        主要是题意要理解清楚
        - 初始 P(power), point 都为0, 目的是获取最大的point
        - 可以通过power 减去 tokens中任一个值(tokens中的值只能使用一次), 使得point 加一
        - 可以通过point 减一, 使得power加上tokens中任一值
        具体的题意解析可以查看 https://leetcode.com/problems/bag-of-tokens/discuss/197856/Bad-descriptions!

        解题思路比较简单:
        - 对tokens进行升序排序
        - 只有power不够用的时候,才考虑拿point去换, 否则一直拿power去换point

        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        if not tokens:
            return 0
        length = len(tokens)
        if length == 1:
            return 0 if P < tokens[0] else 1
        sorted_tokens = sorted(tokens)
        idx, end = 0, length - 1
        point = 0
        while idx < end:
            if P < sorted_tokens[idx]:
                if point == 0:
                    return 0
                P += (sorted_tokens[end] - sorted_tokens[idx])
                end -= 1
                idx += 1
            else:
                P -= sorted_tokens[idx]
                idx += 1
                point += 1
        if P >= sorted_tokens[idx]:
            return point + 1
        return point








