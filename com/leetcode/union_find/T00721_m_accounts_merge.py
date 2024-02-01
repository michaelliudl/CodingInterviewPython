from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def cache():
            for i in range(n):
                acc=accounts[i]
                for j in range(1,len(acc)):
                    email=acc[j]
                    if email in d:
                        d[email].append(i)
                    else:
                        d[email]=[i]

        if not accounts: return accounts
        n,d,merged=len(accounts),{},{}
        cache()
        ans=[]
        for email,indices in d.items():
            if not indices[0] in merged:
                acc=[email]
                for index in indices:
                    for i in range(1,len(accounts[index])):
                        if accounts[index][i]!=email:
                            acc.append(accounts[index][i])
                    merged[index]=1
                acc.sort()
                acc.insert(0,accounts[indices[0]][0])
                ans.append(acc)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testAccountsMerge(self):
        s = Solution()
        self.assertEqual(s.accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]), 
                         [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
        self.assertEqual(s.accountsMerge(accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]), 
                         [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]])
        


if __name__ == '__main__':
    unittest.main()