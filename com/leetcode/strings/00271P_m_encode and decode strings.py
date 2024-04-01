from typing import List

'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).
'''

class Codec:
    
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join(str(len(string)) + '\0' + string for string in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        start = 0
        i = 0
        while i < len(s):
            if s[i] != '\0':
                i += 1
                continue
            length = int(s[start:i])
            start = i + 1 + length
            string = s[(i+1):start]
            result.append(string)
            i = start
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

class Solution:
    pass
                       


import unittest

class TestSolution(unittest.TestCase):
    def testCodec(self):
        c = Codec()
        self.assertEqual(c.decode(c.encode(["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "])), 
                         ["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "])
        self.assertEqual(c.decode(c.encode(["Hello","World"])), ["Hello","World"])
        

if __name__ == '__main__':
    unittest.main()