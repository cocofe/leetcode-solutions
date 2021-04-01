
# @Title: 下一个更大元素 III (Next Greater Element III)
# @Author: cocofe
# @Date: 2021-03-06 00:56:54
# @Runtime: 4 ms
# @Memory: 13 MB

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        1234
        1243
        4321
        # 找到一个最近的, 小的元素 交换, 把低位的较大元素, 与高位的较小元素交换
        12432
        22431
        13422
        s = str(n)
        right = len(s) - 1
        prev = None
        ans = float('inf')
        while right >= 0:
            if prev is not None:
                if prev > s[right]:
                    break
                elif prev == s[right]:
                    right -= 1
                    continue
            idx = right - 1
            while idx >= 0:
                if s[idx] >= s[right]:
                    idx -= 1
                    continue
                tmp = list(s)
                tmp[idx], tmp[right] = tmp[right], tmp[idx]
                _ans = ''.join(tmp[:idx+1]+sorted(tmp[idx+1:]))
                ans = min(ans, int(_ans))
                break
            prev = s[right]
            right -= 1
        return ans if ans != float('inf') and ans <= 2**31 - 1 else -1
