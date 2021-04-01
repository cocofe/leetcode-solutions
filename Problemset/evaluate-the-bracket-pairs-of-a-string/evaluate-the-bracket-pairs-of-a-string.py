
# @Title: 替换字符串中的括号内容 (Evaluate the Bracket Pairs of a String)
# @Author: cocofe
# @Date: 2021-03-28 11:19:27
# @Runtime: 296 ms
# @Memory: 57.3 MB

class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        key_map = {key: val for key, val in knowledge}
        stack = []
        for c in s:
            if c == ')':
                items = []
                while stack:
                    item = stack.pop()
                    if item == '(':
                        break
                    items.append(item)
                key = ''.join(items[::-1])
                stack.append(key_map.get(key, '?'))
            else:
                stack.append(c)
        return ''.join(stack)
        
