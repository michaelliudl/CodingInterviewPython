from typing import List

'''
We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.

Return true if sentence1 and sentence2 are similar, or false if they are not similar.

Two sentences are similar if:

They have the same length (i.e., the same number of words)
sentence1[i] and sentence2[i] are similar.
Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words a and b are similar, and the words b and c are similar, a and c are not necessarily similar.
'''

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        similar = {}
        for sim1, sim2 in similarPairs:
            if sim1 not in similar:
                similar[sim1] = set()
            if sim2 not in similar:
                similar[sim2] = set()
            similar[sim1].add(sim2)
            similar[sim2].add(sim1)
        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]
            if word1 == word2:
                continue
            if word1 in similar and word2 in similar and word1 in similar[word2] and word2 in similar[word1]:
                continue
            return False
        return True
    
import unittest

class TestSolution(unittest.TestCase):
    def testAreSentencesSimilar(self):
        s = Solution()
        self.assertEqual(s.areSentencesSimilar(sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]), True)
        self.assertEqual(s.areSentencesSimilar(sentence1 = ["great"], sentence2 = ["great"], similarPairs = []), True)
        self.assertEqual(s.areSentencesSimilar(sentence1 = ["great"], sentence2 = ["doubleplus","good"], similarPairs = [["great","doubleplus"]]), False)
        self.assertEqual(s.areSentencesSimilar(sentence1 = ["an","extraordinary","meal"], 
                                               sentence2 = ["one","good","dinner"], 
                                               similarPairs = [["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]]), 
                                               True)


if __name__ == '__main__':
    unittest.main()
