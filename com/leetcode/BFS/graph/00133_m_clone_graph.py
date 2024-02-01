from typing import List,Deque,Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node
        nodeClone=Node()
        visited={}
        q=Deque()
        q.append((node,nodeClone))
        visited[node]=nodeClone
        while q:
            curNode,curNodeClone=q.popleft()
            curNodeClone.val=curNode.val
            for _ in range(len(curNode.neighbors)):
                curNodeClone.neighbors.append(Node())
            for i in range(len(curNode.neighbors)):
                nodeNeighbor=curNode.neighbors[i]
                neighborClone=curNodeClone.neighbors[i]
                if nodeNeighbor in visited:
                    curNodeClone.neighbors[i]=visited[nodeNeighbor]
                else:
                    q.append((nodeNeighbor,neighborClone))
                    visited[nodeNeighbor]=neighborClone
        return nodeClone
        

import unittest

class TestSolution(unittest.TestCase):
    def testCloneGraph(self):
        s = Solution()
        node1=Node(1,[])
        node2=Node(2,[])
        node3=Node(3,[])
        node4=Node(4,[])
        node1.neighbors.append(node2)
        node1.neighbors.append(node4)
        node2.neighbors.append(node1)
        node2.neighbors.append(node3)
        node3.neighbors.append(node2)
        node3.neighbors.append(node4)
        node4.neighbors.append(node1)
        node4.neighbors.append(node3)
        s.cloneGraph(node1)
        


if __name__ == '__main__':
    unittest.main()