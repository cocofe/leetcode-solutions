
# @Title: 实现 Trie (前缀树) (Implement Trie (Prefix Tree))
# @Author: cocofe
# @Date: 2020-08-24 12:52:21
# @Runtime: 292 ms
# @Memory: 27.9 MB

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word:
            if w in node:
                node = node[w]
            else:
                node[w] = {}
                node = node[w]
        node['is_word'] = True  

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for w in word:
            if w in node:
                node = node[w]
            else:
                return False
        return node.get('is_word', False)


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for w in prefix:
            if w in node:
                node = node[w]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
