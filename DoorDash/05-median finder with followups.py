# find running median of a data stream
# case 1: data stream contains only nums btw 0 and 100
# case 2: 99% nums are btw 0 to 100

# Ref: https://leetcode.com/problems/find-median-from-data-stream/

class MedianSearch:
    def __init__(self):
        self.middle = [0] * 101
        self.middle_ct = 0
        self.left = []
        self.right = []

    def add_num(self, num):
        if num < 0:
            self.edge_insert(self.left, num)
        elif num > 100:
            self.edge_insert(self.right, num)
        else:
            self.middle[num] += 1
            self.middle_ct += 1

    def add_num2(self, num):
        self.middle[num] += 1
        self.middle_ct += 1

    def get_median2(self):
        first = second = None
        if self.middle_ct % 2 != 0:
            first = (self.middle_ct // 2) + 1
        else:
            first = (self.middle_ct // 2)
            second = first + 1

        first_val = second_val = None
        curr = 0
        ith = 0
        while ith < len(self.middle):
            curr += self.middle[ith]
            if curr >= first:
                first_val = ith
                if second is not None:
                    if curr >= second:
                        second_val = first_val
                    else:
                        ith += 1
                        while ith < len(self.middle):
                            curr += self.middle[ith]
                            if curr >= second:
                                second_val = ith
                                break
                            ith += 1
                break
            ith += 1

        if second is None:
            return first_val
        else:
            return (first_val + second_val) / 2


    def edge_insert(self, arr, num):
        arr.append(num)
        i = len(arr) - 1
        while i > 0 and arr[i - 1] > num:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1

    def get_median(self):
        total_nums = self.middle_ct + len(self.left) + len(self.right)
        first = (total_nums // 2) + 1
        second = None

        if total_nums % 2 == 0:
            second = first - 1

        first_val = self.find_idx(first)
        if second is not None:
            second_val = self.find_idx(second)
        else:
            return first_val

        return (first_val + second_val) / 2

    def find_idx(self, ith):
        if ith <= len(self.left):
            return self.left[ith - 1]
        elif ith > len(self.left) + self.middle_ct:
            return self.right[ith - len(self.left) - self.middle_ct - 1]
        else:
            curr_ct = len(self.left)
            for ith_val in range(0, 101):
                if self.middle[ith_val] + curr_ct >= ith:
                    return ith_val
                curr_ct += self.middle[ith_val]


if __name__ == '__main__':
    ms = MedianSearch()

    input = [
        ('add_num', 5), ('add_num', 0), ('get_median'), ('add_num', 99),
        ('add_num', 50), ('add_num', 20), ('get_median'), ('add_num', 19),
        ('add_num', 5), ('add_num', 95), ('get_median'), ('add_num', 0),
        ('add_num', 100), ('add_num', 20), ('get_median'), ('add_num', 19),
    ]

    queries = [
        "addNum","findMedian","addNum","findMedian","addNum",
        "findMedian","addNum","findMedian","addNum","findMedian",
        "addNum", "findMedian", "addNum", "findMedian","addNum", "findMedian"
    ]
    values = [[-1],[],[-2],[],[-3],[],[-4],[],[-5],[]]

    values = [
        [-1],[],[2],[],[3],[],[4],[],[5],[],
        [100], [], [33], [], [333], []
    ]

    values = [
        [1],[],[-2],[],[-3],[],[4],[],[5],[],
        [100], [], [332], [], [133], []
    ]
    # values = [
    #     [1],[],[2],[],[3],[],[4],[],[5],[],
    #     [100], [], [33], [], [33], []
    # ]

    # queries = ["addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]

    # values = [[155],[],[66],[],[114],[],[0],[],[60],[],[73],[],[109],[],[26],[],[154],[],[0],[],[107],[],[75],[],[9],[],[57],[],[53],[],[6],[],[85],[],[151],[],[12],[],[110],[],[64],[],[103],[],[42],[],[103],[],[126],[],[3],[],[88],[],[142],[],[79],[],[88],[],[147],[],[47],[],[134],[],[27],[],[82],[],[95],[],[26],[],[124],[],[71],[],[79],[],[130],[],[91],[],[131],[],[67],[],[64],[],[16],[],[60],[],[156],[],[9],[],[65],[],[21],[],[66],[],[49],[],[108],[],[80],[],[17],[],[159],[],[24],[],[90],[],[79],[],[31],[],[79],[],[113],[],[39],[],[54],[],[156],[],[139],[],[8],[],[90],[],[19],[],[10],[],[50],[],[89],[],[77],[],[83],[],[13],[],[3],[],[71],[],[52],[],[21],[],[50],[],[120],[],[159],[],[45],[],[22],[],[69],[],[144],[],[158],[],[19],[],[109],[],[52],[],[50],[],[51],[],[62],[],[20],[],[22],[],[71],[],[95],[],[47],[],[12],[],[21],[],[32],[],[17],[],[130],[],[109],[],[8],[],[61],[],[13],[],[48],[],[107],[],[14],[],[122],[],[62],[],[54],[],[70],[],[96],[],[11],[],[141],[],[129],[],[157],[],[136],[],[41],[],[40],[],[78],[],[141],[],[16],[],[137],[],[127],[],[19],[],[70],[],[15],[],[16],[],[65],[],[96],[],[157],[],[111],[],[87],[],[95],[],[52],[],[42],[],[12],[],[60],[],[17],[],[20],[],[63],[],[56],[],[37],[],[129],[],[67],[],[129],[],[106],[],[107],[],[133],[],[80],[],[8],[],[56],[],[72],[],[81],[],[143],[],[90],[],[0],[]]

    for i in range(len(queries)):
        query = queries[i]

        if query == 'addNum':
            value = values[i][0]
            ms.add_num(value)
        else:
            print(ms.get_median())
