
# @Title: 令牌放置 (Bag of Tokens)
# @Author: cocofe
# @Date: 2019-02-11 21:19:03
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
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
                
                
            
                
                    
                
                
        
