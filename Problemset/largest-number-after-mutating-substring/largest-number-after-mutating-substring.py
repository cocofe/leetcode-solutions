
# @Title: 子字符串突变后可能得到的最大整数 (Largest Number After Mutating Substring)
# @Author: cocofe
# @Date: 2021-07-25 11:20:32
# @Runtime: 180 ms
# @Memory: 22.3 MB

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        up_nums = set()
        ss = list(num)
        nochange = set()
        for idx, num in enumerate(change):
            if num > idx:
                up_nums.add(idx)
            elif num == idx:
                nochange.add(idx)
        for idx, s in enumerate(ss):
            if int(s) not in up_nums:
                continue
            while idx < len(ss) and (int(ss[idx]) in up_nums or int(ss[idx]) in nochange):
                # print('replace {}'.format(idx))
                val = ss[idx]
                ss[idx] = str(change[int(val)])
                idx += 1
            break
        return ''.join(ss)
                
            
        
