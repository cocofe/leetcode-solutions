
# @Title: 好数对的数目 (Number of Good Pairs)
# @Author: cocofe
# @Date: 2020-08-17 02:01:31
# @Runtime: 16 ms
# @Memory: 12.5 MB

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = {}
        for idx, num in enumerate(nums):
            tmp.setdefault(num, [])
            tmp[num].append(idx)
        count = 0
        for key, val in tmp.items():
            length = len(val)
            if length < 2:
                continue
            count += (length * (length - 1)) / 2
        return count
            
            

