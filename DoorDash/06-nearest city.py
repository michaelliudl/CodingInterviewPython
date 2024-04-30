# Ref: https://leetcode.com/discuss/interview-question/1379696/DoorDASH-Onsite

import collections, random


def find_nearest_cities(x_list, y_list, cities, query_cities):
    xi = collections.defaultdict(list)
    yi = collections.defaultdict(list)
    city_cords = {}
    for x, y, c in zip(x_list, y_list, cities):
        xi[x].append((y, c))
        yi[y].append((x, c))
        city_cords[c] = (x, y)

    for xk in xi.keys():
        xi[xk].sort()

    for yk in yi.keys():
        yi[yk].sort()

    ans = []
    for q_city in query_cities:
        if q_city not in city_cords:
            ans.append(None)

        x, y = city_cords[q_city]
        nearest_city = get_nearest_city(xi, yi, x, y, q_city)
        ans.append(nearest_city)

    return ans


def get_nearest_city(xi, yi, x, y, q_city):
    mins = {
        'city': None,
        'dist': float('inf'),
    }

    find_mins(0, len(xi[x]) - 1, xi[x], y, q_city, mins)
    find_mins(0, len(yi[y]) - 1, yi[y], x, q_city, mins)

    return mins['city']


def find_mins(left, right, axis_n_cities, axis_to_compare, q_city, mins):
    while left <= right:
        mid = random.randint(left, right)
        mid_city = axis_n_cities[mid][1]
        mid_axis = axis_n_cities[mid][0]

        if mid_city == q_city:
            if mid > 0:
                mid_city = axis_n_cities[mid - 1][1]
                mid_axis = axis_n_cities[mid - 1][0]
                mid_dist = abs(axis_to_compare - mid_axis)
                update_mins(mid_dist, mid_city, mins)

            if mid < len(axis_n_cities) - 1:
                mid_city = axis_n_cities[mid + 1][1]
                mid_axis = axis_n_cities[mid + 1][0]
                mid_dist = abs(axis_to_compare - mid_axis)
                update_mins(mid_dist, mid_city, mins)

            break

        if mid_axis < axis_to_compare:
            left = mid + 1
        else:
            right = mid - 1


def update_mins(mid_dist, mid_city, mins):
    if mid_dist < mins['dist']:
        mins['dist'] = mid_dist
        mins['city'] = mid_city
    elif mid_dist ==  mins['dist']:
        mins['city'] = min(mins['city'], mid_city)


if __name__ == '__main__':
    cities = ['axx', 'axy', 'az', 'axd', 'aa', 'abc', 'abs']
    xs = [0, 1, 2, 4, 5, 0, 1]
    ys = [1, 2, 5 ,3, 4, 2, 0]

    query_cities = ['axx', 'axy', 'abs']

    nearest_cities = find_nearest_cities(xs, ys, cities, query_cities)
    print(nearest_cities)
