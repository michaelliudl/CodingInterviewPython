# Ref: https://leetcode.com/discuss/interview-question/1293040/Doordash-or-Phone-Screen-or-Software-Engineer-E4-or-Closest-Drivers-to-Restaurant

import random


class Dasher:
    def __init__(self, id, lastLocation, rating):
        self.id = id
        self.lastLocation = lastLocation
        self.rating = rating


class Location:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude


def GetDashers():
    loc1 = Location(1, 3)
    d1 = Dasher(1, loc1, 4)
    loc2 = Location(2, 2)
    d2 = Dasher(2, loc2, 4)
    loc3 = Location(4, 0)
    d3 = Dasher(3, loc3, 4)
    loc4 = Location(1, 1)
    d4 = Dasher(4, loc4, 5)

    loc5 = Location(4, 3)
    d5 = Dasher(5, loc1, 2)
    loc6 = Location(7, 2)
    d6 = Dasher(6, loc6, 4)
    loc7 = Location(4, 0)
    d7 = Dasher(7, loc3, 4)
    loc8 = Location(1, 1)
    d8 = Dasher(8, loc4, 3)

    return [d1, d2, d3, d4, d5, d6, d7, d8]


def find_k_closest_drivers(k):
    dashers = GetDashers()
    quick_select(0, len(dashers) - 1, dashers, k)

    return dashers[:k]


def quick_select(left, right, dashers, k):
    while left <= right:
        pivot = random.randint(left, right)
        pivot = partition(pivot, left, right, dashers)

        if pivot == k:
            return
        elif pivot < k:
            left = pivot + 1
        else:
            right = pivot - 1


def get_sum_hash(dasher):
    loc = dasher.lastLocation
    return (loc.longitude ** 2 + loc.latitude ** 2, - dasher.rating)


def partition(pivot, left, right, dashers):
    pivot_ele = get_sum_hash(dashers[pivot])
    dashers[right], dashers[pivot] = dashers[pivot], dashers[right]

    store_idx = left
    for idx in range(left, right):
        if get_sum_hash(dashers[idx]) < pivot_ele:
            dashers[store_idx], dashers[idx] = dashers[idx], dashers[store_idx]
            store_idx += 1

    dashers[store_idx], dashers[right] = dashers[right], dashers[store_idx]

    return store_idx


if __name__ == '__main__':
    howmany_dashers = 3
    dashers = find_k_closest_drivers(howmany_dashers)

    for dasher in dashers:
        print(
            f'dasher_id: {dasher.id}, rating: {dasher.rating},'
            f'location: {dasher.lastLocation.latitude},'
            f' {dasher.lastLocation.longitude}'
        )
