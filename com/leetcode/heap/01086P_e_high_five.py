from typing import List
import heapq

'''
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

'''

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        if not items:
            return []
        scores = {}
        for id, score in items:
            if id not in scores:
                scores[id] = []
            scores[id].append(score)
        result = []
        for id, score in scores.items():
            score.sort(reverse=True)
            result.append([id, sum(score[:5]) // 5])
        result.sort()
        return result
        



import unittest

class TestSolution(unittest.TestCase):
    def testHighFive(self):
        s = Solution()
        self.assertEqual(s.highFive(items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]), [[1,87],[2,88]])
        self.assertEqual(s.highFive(items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]), [[1,100],[7,100]])
        self.assertEqual(s.highFive(items = [[1,89],[1,58],[1,77],[1,8],[1,98],[1,0],[1,54],[1,44],[1,31],[1,34],[1,43],[1,59],[1,0],[1,7],[1,39],[1,51],[1,50],[1,87],[1,93],[1,88],[2,75],[2,14],[2,35],[2,37],[2,17],[2,0],[2,84],[2,89],[2,11],[2,93],[2,53],[2,14],[2,96],[2,18],[2,20],[2,99],[2,47],[2,9],[2,41],[2,40],[3,72],[3,41],[3,54],[3,45],[3,27],[3,0],[3,33],[3,9],[3,78],[3,37],[3,33],[3,16],[3,81],[3,48],[3,54],[3,21],[3,31],[3,24],[3,87],[3,72],[4,99],[4,98],[4,3],[4,7],[4,15],[4,21],[4,44],[4,57],[4,60],[4,80],[4,71],[4,53],[4,41],[4,16],[4,37],[4,93],[4,5],[4,58],[4,48],[4,70],[5,93],[5,61],[5,94],[5,50],[5,94],[5,0],[5,40],[5,49],[5,85],[5,100],[5,35],[5,17],[5,49],[5,74],[5,86],[5,79],[5,51],[5,30],[5,45],[5,91],[6,41],[6,58],[6,48],[6,34],[6,12],[6,20],[6,20],[6,28],[6,3],[6,7],[6,75],[6,6],[6,86],[6,89],[6,48],[6,75],[6,39],[6,14],[6,59],[6,82],[7,87],[7,2],[7,86],[7,23],[7,49],[7,55],[7,72],[7,19],[7,79],[7,40],[7,47],[7,52],[7,78],[7,78],[7,84],[7,24],[7,1],[7,70],[7,75],[7,91],[8,93],[8,73],[8,83],[8,69],[8,78],[8,85],[8,100],[8,2],[8,53],[8,67],[8,3],[8,26],[8,10],[8,8],[8,68],[8,67],[8,45],[8,61],[8,77],[8,23],[9,53],[9,95],[9,34],[9,69],[9,57],[9,68],[9,87],[9,81],[9,10],[9,86],[9,25],[9,51],[9,98],[9,18],[9,58],[9,57],[9,60],[9,41],[9,75],[9,93],[10,9],[10,13],[10,2],[10,58],[10,32],[10,95],[10,82],[10,52],[10,12],[10,25],[10,32],[10,77],[10,0],[10,8],[10,92],[10,67],[10,25],[10,26],[10,90],[10,31],[11,79],[11,76],[11,20],[11,77],[11,87],[11,16],[11,2],[11,99],[11,56],[11,66],[11,20],[11,36],[11,54],[11,10],[11,3],[11,98],[11,97],[11,2],[11,81],[11,73],[12,44],[12,3],[12,8],[12,15],[12,6],[12,17],[12,45],[12,97],[12,40],[12,10],[12,66],[12,26],[12,5],[12,34],[12,89],[12,95],[12,21],[12,47],[12,78],[12,79],[13,38],[13,9],[13,82],[13,78],[13,65],[13,98],[13,72],[13,91],[13,22],[13,58],[13,56],[13,48],[13,95],[13,61],[13,43],[13,36],[13,67],[13,68],[13,60],[13,12],[14,84],[14,82],[14,54],[14,60],[14,68],[14,7],[14,71],[14,79],[14,78],[14,42],[14,25],[14,70],[14,6],[14,38],[14,60],[14,21],[14,64],[14,77],[14,6],[14,22],[15,75],[15,27],[15,96],[15,29],[15,33],[15,46],[15,9],[15,65],[15,70],[15,94],[15,85],[15,80],[15,1],[15,61],[15,7],[15,42],[15,43],[15,54],[15,51],[15,1],[16,34],[16,23],[16,20],[16,3],[16,26],[16,37],[16,46],[16,73],[16,38],[16,25],[16,85],[16,13],[16,42],[16,49],[16,5],[16,45],[16,26],[16,27],[16,87],[16,77],[17,7],[17,22],[17,91],[17,55],[17,24],[17,62],[17,100],[17,6],[17,80],[17,5],[17,73],[17,70],[17,34],[17,14],[17,39],[17,68],[17,16],[17,97],[17,89],[17,39],[18,67],[18,99],[18,82],[18,72],[18,98],[18,70],[18,78],[18,71],[18,41],[18,26],[18,44],[18,29],[18,91],[18,69],[18,11],[18,59],[18,67],[18,23],[18,39],[18,19],[19,34],[19,64],[19,30],[19,85],[19,42],[19,40],[19,1],[19,1],[19,50],[19,74],[19,47],[19,25],[19,89],[19,39],[19,74],[19,64],[19,34],[19,7],[19,26],[19,78],[20,40],[20,60],[20,87],[20,94],[20,34],[20,22],[20,76],[20,94],[20,52],[20,10],[20,23],[20,99],[20,64],[20,35],[20,36],[20,62],[20,37],[20,10],[20,64],[20,65],[21,47],[21,15],[21,86],[21,24],[21,56],[21,62],[21,98],[21,90],[21,72],[21,13],[21,37],[21,8],[21,57],[21,43],[21,18],[21,29],[21,88],[21,45],[21,56],[21,76],[22,30],[22,8],[22,46],[22,13],[22,16],[22,82],[22,59],[22,77],[22,81],[22,30],[22,51],[22,8],[22,54],[22,48],[22,56],[22,49],[22,40],[22,87],[22,26],[22,57],[23,77],[23,29],[23,44],[23,64],[23,3],[23,79],[23,88],[23,36],[23,41],[23,98],[23,19],[23,38],[23,13],[23,99],[23,84],[23,75],[23,85],[23,43],[23,11],[23,68],[24,80],[24,73],[24,38],[24,24],[24,8],[24,67],[24,39],[24,79],[24,11],[24,94],[24,77],[24,62],[24,2],[24,87],[24,76],[24,2],[24,17],[24,31],[24,31],[24,89],[25,86],[25,38],[25,9],[25,36],[25,97],[25,94],[25,24],[25,7],[25,8],[25,15],[25,80],[25,0],[25,86],[25,72],[25,42],[25,36],[25,20],[25,21],[25,87],[25,6],[26,74],[26,29],[26,69],[26,88],[26,2],[26,10],[26,85],[26,45],[26,76],[26,96],[26,54],[26,16],[26,80],[26,53],[26,81],[26,37],[26,15],[26,44],[26,90],[26,60],[27,92],[27,87],[27,21],[27,38],[27,10],[27,2],[27,88],[27,52],[27,44],[27,66],[27,26],[27,57],[27,65],[27,51],[27,30],[27,65],[27,94],[27,0],[27,57],[27,51],[28,65],[28,55],[28,28],[28,59],[28,12],[28,3],[28,16],[28,99],[28,18],[28,12],[28,15],[28,27],[28,62],[28,84],[28,66],[28,45],[28,30],[28,96],[28,2],[28,41],[29,1],[29,34],[29,53],[29,82],[29,58],[29,95],[29,60],[29,91],[29,48],[29,84],[29,57],[29,40],[29,29],[29,43],[29,96],[29,34],[29,81],[29,30],[29,59],[29,12],[30,61],[30,68],[30,100],[30,68],[30,4],[30,18],[30,97],[30,0],[30,89],[30,66],[30,78],[30,15],[30,46],[30,59],[30,8],[30,38],[30,67],[30,0],[30,36],[30,10],[31,22],[31,87],[31,83],[31,21],[31,36],[31,60],[31,64],[31,65],[31,16],[31,51],[31,93],[31,10],[31,35],[31,19],[31,100],[31,61],[31,67],[31,58],[31,0],[31,78],[32,46],[32,49],[32,15],[32,77],[32,33],[32,100],[32,95],[32,63],[32,17],[32,100],[32,95],[32,97],[32,93],[32,31],[32,58],[32,53],[32,48],[32,24],[32,27],[32,38],[33,58],[33,67],[33,15],[33,35],[33,68],[33,31],[33,90],[33,43],[33,38],[33,77],[33,30],[33,27],[33,87],[33,78],[33,73],[33,78],[33,71],[33,84],[33,90],[33,53],[34,13],[34,36],[34,21],[34,13],[34,44],[34,100],[34,95],[34,93],[34,16],[34,85],[34,20],[34,58],[34,5],[34,18],[34,21],[34,14],[34,48],[34,32],[34,87],[34,10],[35,91],[35,100],[35,57],[35,99],[35,1],[35,38],[35,21],[35,73],[35,32],[35,15],[35,53],[35,17],[35,43],[35,37],[35,92],[35,30],[35,49],[35,49],[35,80],[35,32],[36,85],[36,56],[36,78],[36,90],[36,39],[36,7],[36,35],[36,29],[36,53],[36,64],[36,88],[36,0],[36,11],[36,42],[36,13],[36,35],[36,24],[36,2],[36,21],[36,76],[37,81],[37,5],[37,18],[37,91],[37,25],[37,41],[37,43],[37,96],[37,80],[37,50],[37,62],[37,99],[37,6],[37,28],[37,54],[37,93],[37,62],[37,89],[37,80],[37,52],[38,9],[38,97],[38,0],[38,27],[38,95],[38,82],[38,47],[38,76],[38,93],[38,7],[38,57],[38,33],[38,19],[38,76],[38,41],[38,83],[38,15],[38,58],[38,96],[38,23],[39,80],[39,49],[39,82],[39,70],[39,30],[39,9],[39,47],[39,8],[39,32],[39,66],[39,92],[39,89],[39,24],[39,48],[39,93],[39,14],[39,15],[39,69],[39,52],[39,47],[40,93],[40,79],[40,2],[40,96],[40,82],[40,48],[40,15],[40,25],[40,70],[40,97],[40,38],[40,75],[40,25],[40,97],[40,73],[40,0],[40,11],[40,86],[40,37],[40,11]]), [[1,91],[2,92],[3,78],[4,88],[5,94],[6,81],[7,85],[8,87],[9,91],[10,87],[11,92],[12,87],[13,88],[14,80],[15,86],[16,74],[17,91],[18,89],[19,80],[20,90],[21,87],[22,77],[23,90],[24,85],[25,90],[26,88],[27,85],[28,82],[29,89],[30,86],[31,88],[32,97],[33,85],[34,92],[35,92],[36,83],[37,93],[38,92],[39,87],[40,93]])
        self.assertEqual(s.highFive(items = [[5,91],[5,92],[3,93],[3,97],[5,60],[3,77],[5,65],[5,87],[5,100],[3,100],[3,76]]), [[3,88],[5,87]])



if __name__ == '__main__':
    unittest.main()