
# @Title: 黑名单中的随机数 (Random Pick with Blacklist)
# @Author: cocofe
# @Date: 2020-09-30 20:47:08
# @Runtime: 6164 ms
# @Memory: 21.2 MB

class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        # 一个(值, 索引) 的 map, 其中索引是指数组[0, N) 中的索引(不用真正去创建这个数组)
        white_end = N - len(blacklist) - 1
        self.idx_val_map = {}
        need_swap_values = []
        for b in blacklist:
            if b > white_end:
                continue
            need_swap_values.append(b)
        end = N - 1
        swap_idx = 0
        for _ in blacklist:
            if end in blacklist:
                end -= 1
                continue
            self.idx_val_map[need_swap_values[swap_idx]] = end
            end -= 1
            swap_idx += 1
        self.length = N - len(blacklist) - 1

    def pick(self):
        """
        :rtype: int
        """
        idx = random.randint(0, self.length)
        return self.idx_val_map.get(idx, idx)


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
