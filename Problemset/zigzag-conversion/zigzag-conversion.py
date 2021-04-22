
# @Title: Z 字形变换 (ZigZag Conversion)
# @Author: cocofe
# @Date: 2021-04-23 03:30:14
# @Runtime: 56 ms
# @Memory: 14.8 MB

class Solution:
    def convert(self, ss: str, nr: int) -> str:
        if nr == 1: return ss
        level = ['' for _ in range(nr)]
        is_down = 0
        idx = 0
        for s in ss:
            level[idx] += s
            if idx == 0 or idx == nr - 1:
                is_down ^= 1
            idx += 1 if is_down else -1
        return ''.join(level)

