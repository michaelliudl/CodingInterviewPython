# print all valid order paths e.g.: delivery after pickup given n

# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

def get_all_patterns(n):
    picked_up = set()
    delivered = set()
    patterns = []
    pattern = []

    find_pattern(picked_up, delivered, pattern, patterns, n)

    return patterns


def find_pattern(picked_up, delivered, pattern, patterns, n):
    if len(pattern) == n * 2:
        patterns.append('->'.join(pattern))
    else:
        for task in range(1, n + 1):
            pickup = 'P' + str(task)
            delivery = 'D' + str(task)

            if pickup not in picked_up:
                picked_up.add(pickup)
                pattern.append(pickup)
                find_pattern(picked_up, delivered, pattern, patterns, n)
                pattern.pop()
                picked_up.remove(pickup)

            if pickup in picked_up and delivery not in delivered:
                delivered.add(delivery)
                pattern.append(delivery)
                find_pattern(picked_up, delivered, pattern, patterns, n)
                pattern.pop()
                delivered.remove(delivery)

if  __name__ == '__main__':
    print(get_all_patterns(3))

# Time:
# O((N) ^ 2*N)
# Space:
# O(2* N)  => O(N) to hold a single pattern
#  2n -1                         5     3  1
# for p: N! for d => p1, p2..pn-1..pn

#   2n-1   2n - 3 ..... 3, 1
# p1     p2....p3..pn

