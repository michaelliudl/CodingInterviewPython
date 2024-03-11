from typing import List

class Solution:

    # TODO Union Find
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        pass

    # Graph and DFS
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # Build graph of emails that each email in original account records are neighbors
        # Build cache from emails to names
        def graph():
            for i in range(n):
                acc=accounts[i]
                name=acc[0]
                for j in range(1,len(acc)):
                    email=acc[j]
                    emailToNames[email]=name
                    if email not in emailGraph:
                        emailGraph[email]=set()
                    for k in range(1,len(acc)):
                        othereEmail=acc[k]
                        if othereEmail!=email:
                            emailGraph[email].add(othereEmail)
                            if othereEmail not in emailGraph:
                                emailGraph[othereEmail]=set()
                            emailGraph[othereEmail].add(email)
        
        def dfs(email, account):
            if email in visited: return 
            visited.add(email)
            account.append(email)
            if email in emailGraph:
                for otherEmail in emailGraph[email]:
                    if otherEmail not in visited:
                        dfs(otherEmail, account)

        if not accounts: return accounts
        n=len(accounts)
        emailToNames={}
        emailGraph={}
        graph()

        ans=[]
        visited=set()
        # Loop through emails
        for email in emailToNames:
            if email not in visited:
                account=[]
                dfs(email,account)
                account.sort()
                account.insert(0, emailToNames[email])
                ans.append(account)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testAccountsMerge(self):
        s = Solution()
        # self.assertEqual(s.accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]), 
        #                  [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
        self.assertEqual(s.accountsMerge(accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
                                                     ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
                                                     ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
                                                     ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
                                                     ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]), 
                         [["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
                          ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
                          ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
                          ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
                          ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]])
        


if __name__ == '__main__':
    unittest.main()