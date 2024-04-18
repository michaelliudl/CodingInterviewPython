from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Prefix sum and use hash table to cache diff nodes
    # Similar to 325, 560, 1658
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-float('inf'), head)
        sumToNode = {0: dummy}
        nodeToSum = {dummy: 0}          # Use another map to track nodes deleted and their prefix sum
        sum = 0
        p = head
        while p:
            sum += p.val
            if sum in sumToNode:
                q = sumToNode[sum]      # Iterate deleted nodes and remove their prefix sum from map
                while q != p:
                    q = q.next
                    if q in nodeToSum:
                        qSum = nodeToSum[q]
                        if qSum in sumToNode:
                            del sumToNode[qSum]
                sumToNode[sum].next = p.next
            else:
                sumToNode[sum] = p
                nodeToSum[p] = sum
            p = p.next
        return dummy.next



import unittest

class TestSolution(unittest.TestCase):
    def testSubarraySum(self):
        s = Solution()
        self.assertEqual(s.subarraySum(nums = [1,-1,0], k = 0), 3)
        self.assertEqual(s.subarraySum(nums = [1,1,1], k = 2), 2)
        self.assertEqual(s.subarraySum(nums = [1,2,3], k = 3), 2)



if __name__ == '__main__':
    unittest.main()