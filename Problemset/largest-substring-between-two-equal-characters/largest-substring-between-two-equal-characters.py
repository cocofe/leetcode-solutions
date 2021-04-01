
# @Title: 两个相同字符之间的最长子字符串 (Largest Substring Between Two Equal Characters)
# @Author: cocofe
# @Date: 2020-10-18 23:21:59
# @Runtime: 12 ms
# @Memory: 12.9 MB

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_idx_map = collections.defaultdict(list)
        for idx, _s in enumerate(s):
            char_idx_map[_s].append(idx)
        ans = -1
        for _s, idxs in char_idx_map.items():
            if len(idxs) < 2:
                continue
            ans = max(idxs[-1] - idxs[0] - 1, ans)
        return ans
            
