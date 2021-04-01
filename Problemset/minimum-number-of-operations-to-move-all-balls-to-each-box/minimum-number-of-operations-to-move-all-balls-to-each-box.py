
# @Title: 移动所有球到每个盒子所需的最小操作数 (Minimum Number of Operations to Move All Balls to Each Box)
# @Author: cocofe
# @Date: 2021-02-21 10:42:45
# @Runtime: 1576 ms
# @Memory: 13.3 MB

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        map = [idx for idx, box in enumerate(boxes) if box == '1']
        ans = []
        for i in range(len(boxes)):
            s = sum([abs(idx - i) for idx in map])
            ans.append(s)
        return ans
