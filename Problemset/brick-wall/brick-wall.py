
# @Title: 砖墙 (Brick Wall)
# @Author: cocofe
# @Date: 2021-05-02 02:20:32
# @Runtime: 60 ms
# @Memory: 17.8 MB

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        mapping = collections.defaultdict(int)
        for w in wall:
            idx = 0
            for i in w[:-1]:
                idx += i
                mapping[idx] += 1
        return len(wall) - max(mapping.values() or [0])

        


            
