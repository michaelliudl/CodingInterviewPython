from typing import List

class TrieNode:

    def __init__(self):
        self.children=[None]*26
        self.word=None

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word):
        node=self.root
        for c in word:
            index = ord(c) - ord('a')
            if not node.children[index]:
                node.children[index]=TrieNode()
            node=node.children[index]
        node.word=word
    
    def search(self, prefix, count):

        def dfs(node, count):
            if len(words)==count:
                return
            if node.word:
                words.append(node.word)
            for child in node.children:
                if child:
                    dfs(child, count)

        node=self.root
        for c in prefix:
            index=ord(c) - ord('a')
            if not node.children[index]:
                return []
            node=node.children[index]
        words=[]
        dfs(node, count)
        return words

class Solution:

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        if not products or not searchWord: return []
        trie=Trie()
        for prod in products:
            trie.insert(prod)
        ans=[]
        for i in range(len(searchWord)):
            ans.append(trie.search(searchWord[:i+1], 3))
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testSuggestedProducts(self):
        s = Solution()
        self.assertEqual(s.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"), 
                         [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]])
        self.assertEqual(s.suggestedProducts(products = ["havana"], searchWord = "havana"), 
                         [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]])


if __name__ == '__main__':
    unittest.main()