
# @Title: 判断句子是否为全字母句 (Check if the Sentence Is Pangram)
# @Author: cocofe
# @Date: 2021-04-18 11:34:41
# @Runtime: 52 ms
# @Memory: 14.9 MB

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
