
# @Title: 比特位计数 (Counting Bits)
# @Author: cocofe
# @Date: 2021-03-03 01:13:54
# @Runtime: 60 ms
# @Memory: 16.8 MB

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for i in range(1, num+1):
            # 右移一位的值肯定已经计算过了, 所以如果最右位为1, 则额外加一
            ans.append(ans[i >> 1] + (i & 1))
        return ans


