__author__ = 'doliu'


def multiples_of_3_and_5():
    return sum([x for x in xrange(1000) if x % 3 == 0 or x % 5 == 0])


def even_fibonacci_number():
    fibo = [1,2]
    cur = 0
    while cur <= 4000000:
        n = len(fibo)
        cur = fibo[n-1] + fibo[n-2]
        fibo.append(cur)
    return sum([x for x in fibo if x % 2 == 0])


if __name__ == "__main__":
    # print(multiples_of_3_and_5())
    print(even_fibonacci_number())

