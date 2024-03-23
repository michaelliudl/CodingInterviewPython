from typing import List

class Solution:

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if not logs:
            return logs
        digitLogs, letterLogs = [], []
        for log in logs:
            words = log.split(' ')
            if '0' <= words[1][0] <= '9':
                digitLogs.append(log)
            else:
                letterLogs.append((' '.join(words[1:]), words[0]))
        letterLogs.sort()
        result = [id + ' ' + content for content, id in letterLogs]
        result.extend(digitLogs)
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testReorderLogFiles(self):
        s = Solution()
        self.assertEqual(s.reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]), 
                         ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])
        self.assertEqual(s.reorderLogFiles(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]), 
                         ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])

if __name__ == '__main__':
    unittest.main()