# Given a streaming data of the form (timestamp, value),
# find the maximum value in the stream in the last X seconds.

# Assume time is monotonically increasing.
# Assume time is in the order of seconds.
# max_value() function finds the max in the last X seconds.

# Ref: https://leetcode.com/discuss/interview-question/1302614/DoorDash-Onsite-Interview-(new-question-again!)

import collections


class StreamProcessor:
    def __init__(self, x):
        self.x = x
        self.deque = collections.deque()

    def set_value(self, t, v):
        while self.deque and t - self.deque[0][0] > self.x:
           self.deque.popleft()

        while self.deque and self.deque[-1][1] < v:
            self.deque.pop()

        self.deque.append((t, v))

    def max_value(self, cur_t): # this will be always current time
        while self.deque and cur_t - self.deque[0][0] > self.x:
            self.deque.popleft()

        if not self.deque:
            return -1

        return self.deque[0][1]


if __name__ == '__main__':
    sp = StreamProcessor(5)
    sp.set_value(0, 5)
    sp.set_value(1, 6)
    sp.set_value(2, 4)
    sp.set_value(5, 5)
    sp.set_value(9, 19)
    sp.set_value(15, 4)
    sp.set_value(16, 25)
    sp.set_value(19, 6)
    sp.set_value(20, 4)

    print(sp.max_value(22))
