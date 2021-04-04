
# @Title: 字母异位词分组 (Group Anagrams)
# @Author: cocofe
# @Date: 2021-04-04 16:56:36
# @Runtime: 72 ms
# @Memory: 19 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = collections.defaultdict(list)
        for idx, string in enumerate(strs):
            string = ''.join(sorted(string))
            mapping[string].append(idx)
        ans = []
        for key, idxs in mapping.items():
            ans.append([strs[idx] for idx in idxs])
        return ans

