
# @Title: 仅含 1 的子串数 (Number of Substrings With Only 1s)
# @Author: cocofe
# @Date: 2020-08-17 03:10:18
# @Runtime: 96 ms
# @Memory: 15.4 MB

class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 0
        tmp = collections.defaultdict(int)
        length = 0
        while j < len(s):
            val = s[j]
            if val == '0':
                if length:
                    tmp[length] += 1
                    length = 0
            else:
                length += 1
            j += 1
        if length:
            tmp[length] += 1
        total_count = 0
        for length, count in tmp.items():
            _c = sum(range(1, length+1)) * count
            total_count += _c
        return total_count % (10 ** 9 + 7)
