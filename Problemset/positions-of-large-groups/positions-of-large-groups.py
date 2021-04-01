
# @Title: 较大分组的位置 (Positions of Large Groups)
# @Author: cocofe
# @Date: 2021-01-05 00:57:28
# @Runtime: 20 ms
# @Memory: 12.9 MB

class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        ans = []
        start, end = None, None
        for i, char in enumerate(s):
            if start is None:
                start = i
            else:
                if char != s[start]:
                    if start is not None and end is not None and (end - start) >= 2:
                        ans.append([start, end])
                    start = i
                    end = None
                else:
                    end = i
        if end is not None and start is not None and (end - start) >= 2:
            ans.append([start, end])
        return ans
