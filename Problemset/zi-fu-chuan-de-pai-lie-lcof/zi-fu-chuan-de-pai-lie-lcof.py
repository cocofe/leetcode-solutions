
# @Title: 字符串的排列 (字符串的排列  LCOF)
# @Author: cocofe
# @Date: 2020-08-16 15:11:36
# @Runtime: 100 ms
# @Memory: 18.9 MB

class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        chars, ans, length = list(s), [], len(s)
        # idx 之前是固定住的, 准备固定idx
        def dfs(idx):
            if idx == length - 1:
                ans.append(''.join(chars))
                return
            to_fixed_chars = set()
            for i in range(idx, length):
                if chars[i] in to_fixed_chars:
                    continue
                to_fixed_chars.add(chars[i])
                # 选择一个字符, 固定在idx位置, 并原有的idx字符进行交换
                chars[i], chars[idx] = chars[idx], chars[i]
                # 固定idx+1位置
                dfs(idx + 1)
                # 恢复chars, 继续选择下一个字符固定在idx位置
                chars[i], chars[idx] = chars[idx], chars[i]
        dfs(0)
        return ans
