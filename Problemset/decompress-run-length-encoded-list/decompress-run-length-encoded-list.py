
# @Title: 解压缩编码列表 (Decompress Run-Length Encoded List)
# @Author: cocofe
# @Date: 2020-01-26 17:29:44
# @Runtime: 64 ms
# @Memory: N/A

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        idx = 0
        while idx + 1 < len(nums):
            freq = nums[idx]
            val = nums[idx+1]
            ret.extend([val] * freq)
            idx += 2
        return ret
        
