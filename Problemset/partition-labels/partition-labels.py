
# @Title: 划分字母区间 (Partition Labels)
# @Author: cocofe
# @Date: 2020-10-22 18:53:32
# @Runtime: 36 ms
# @Memory: 13 MB

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        mapping = collections.defaultdict(list)
        for idx, s in enumerate(S):
            idxs = mapping[s]
            if len(idxs) < 2:
                mapping[s].append(idx)
            else:
                mapping[s][1] = idx
        ans = []
        idx = 0
        while idx < len(S):
            idxs = mapping[S[idx]]
            if len(idxs) == 1:
                ans.append(1)
                idx += 1
            else:
                start, end = idxs
                idx += 1
                while idx <= end:
                    idxs = mapping[S[idx]]
                    end = max(end, idxs[-1])
                    idx += 1
                ans.append(idx - start)
        return ans



        
        
