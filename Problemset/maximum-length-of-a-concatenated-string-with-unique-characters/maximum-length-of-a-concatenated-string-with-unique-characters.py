
# @Title: 串联字符串的最大长度 (Maximum Length of a Concatenated String with Unique Characters)
# @Author: cocofe
# @Date: 2021-06-19 02:28:48
# @Runtime: 96 ms
# @Memory: 15.2 MB

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 要清楚是数组的子序列拼接成字符串, 不是数组元素的子序列互相拼接
        masks = []
        for s in arr:
            mask = 0
            for ch in s:
                if mask >> (ord(ch) - ord('a')) & 1 == 1:
                    mask = 0
                    break
                mask |= 1 << (ord(ch) - ord('a'))
            if mask:
                masks.append(mask)
        ans = 0
        def backtrace(idx, mask):
            if idx == len(masks):
                nonlocal ans
                ans = max(ans, bin(mask).count('1'))
                return
            if mask == 0 or (masks[idx] ^ mask) & mask == mask:
                backtrace(idx+1, mask | masks[idx])
            backtrace(idx+1, mask)
        backtrace(0, 0)
        return ans
        

            
