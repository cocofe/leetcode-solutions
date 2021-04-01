
# @Title: 1比特与2比特字符 (1-bit and 2-bit Characters)
# @Author: cocofe
# @Date: 2020-03-17 15:55:27
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        idx = 0
        last = False
        while idx < len(bits):
            if bits[idx] == 0:
                idx += 1
                last = True
            else:
                idx += 2
                last = False
        return last
                
        
