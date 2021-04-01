
# @Title: 根据身高重建队列 (Queue Reconstruction by Height)
# @Author: cocofe
# @Date: 2021-03-09 00:13:32
# @Runtime: 32 ms
# @Memory: 13.6 MB

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 按照身高降序, 位置升序
        # 可以这么理解, 前面看不到比自己矮的人, 所以先把高个子的插入, 矮个子的人插入其中是不会影响已插入的高个子可以看到的人数
        ans = []
        people = sorted(people, key=lambda p: (-p[0], p[1]))
        for p in people:
            if p[1] >= len(ans):
                ans.append(p)
            else:
                ans.insert(p[1], p)
        return ans
