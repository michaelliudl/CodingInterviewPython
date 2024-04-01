from typing import Optional,List,Deque
class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens:
            self.renew(tokenId, currentTime)
        if tokenId not in self.tokens:
            self.tokens[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokens:
            return
        if self.tokens[tokenId] <= currentTime:
            del self.tokens[tokenId]
            return
        self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        result = 0
        expId = set()
        for tokenId, expirationTime in self.tokens.items():
            if expirationTime <= currentTime:
                expId.add(tokenId)
            else:
                result += 1
        for tokenId in expId:
            del self.tokens[tokenId]
        return result


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):

    def testAuthenticationManager(self):
        am = AuthenticationManager()
        am.mkdir('/m')
        self.assertEqual(am.ls('/m'), [])
        am.mkdir('/w')
        self.assertEqual(am.ls('/'), ['m','w'])
        self.assertEqual(am.ls('/w'), [])
        self.assertEqual(am.ls('/'), ['m','w'])
        am.addContentToFile('/dycete', 'emer')
        self.assertEqual(am.ls('/w'), [])
        self.assertEqual(am.ls('/'), ['dycete', 'm','w'])
        self.assertEqual(am.ls('/dycete'), ['dycete'])

    def testFileSystem3(self):
        fs = FileSystem()
        fs.mkdir('/zijzllb')
        self.assertEqual(fs.ls('/'), ['zijzllb'])
        self.assertEqual(fs.ls('/zijzllb'), [])
        fs.mkdir('/r')
        self.assertEqual(fs.ls('/'), ['r', 'zijzllb'])
        self.assertEqual(fs.ls('/r'), [])
        fs.addContentToFile('/zijzllb/hfktg', 'd')
        self.assertEqual(fs.readContentFromFile('/zijzllb/hfktg'), 'd')
        self.assertEqual(fs.ls('/'), ['r', 'zijzllb'])
        self.assertEqual(fs.readContentFromFile('/zijzllb/hfktg'), 'd')

    def testFileSystem1(self):
        fs = FileSystem()
        self.assertEqual(fs.ls('/'), [])
        fs.mkdir('/a/b/c')
        fs.addContentToFile('/a/b/c/d', 'hello')
        self.assertEqual(fs.ls('/'), ['a'])
        self.assertEqual(fs.readContentFromFile('/a/b/c/d'), 'hello')

    def testFileSystem2(self):
        fs = FileSystem()
        self.assertEqual(fs.ls('/'), [])
        fs.mkdir('/a/b/c')
        self.assertEqual(fs.ls('/a/b'), ['c'])

if __name__ == '__main__':
    unittest.main()