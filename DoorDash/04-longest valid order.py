# Find longest valid subarray

# Ex 1: orders = ['P1', 'P1', 'D1'], return ['P1', 'D1']
# Ex 2: orders = ['P1', 'P1', 'D1', 'D1'], return ['P1', 'D1']

# Ref: https://leetcode.com/discuss/interview-question/914113/Longest-valid-orders-path-(Doordash)



def longest_valid_order(orders):
    longest_idxs = [0, 0]

    for start in range(len(orders)):
        for end in range(start + 1, len(orders)):
            pickups = set()
            deliveries = set()
            is_valid = True

            for idx in range(start, end + 1):
                order_type = orders[idx][0]
                order_id = orders[idx][1:]

                if order_type == 'P':
                    if order_id not in pickups and order_id not in deliveries:
                        pickups.add(order_id)
                    else:
                        is_valid = False
                        break
                else:
                    if order_id in pickups and order_id not in deliveries:
                        deliveries.add(order_id)
                    else:
                        is_valid = False
                        break

            if is_valid and len(pickups) == len(deliveries):
                update_logest_idxs(longest_idxs, start, end + 1)

    ans = []
    for idx in range(longest_idxs[0], longest_idxs[1]):
        ans.append(orders[idx])

    print(ans)


def update_logest_idxs(longest_idxs, start, end):
    if longest_idxs[1] - longest_idxs[0] < end - start:
        longest_idxs[0] = start
        longest_idxs[1] = end


if __name__ == '__main__':
    orders = ['P1', 'P1', 'P2', 'D3', 'P1', 'P2', 'D2', 'D1', 'P4', 'D3', 'D1']
    longest_valid_order(orders)
