# Ref: https://leetcode.com/discuss/interview-question/1387937/Doordash-new-Q

def get_increments(times):
    days = {
        'mon': 1,
        'tue': 2,
        'wed': 3,
        'thu': 4,
        'fri': 5,
        'sat': 6,
        'sun': 7,
    }

    start = clean_time(times[0], days)
    end = clean_time(times[1], days, True)

    end_borders = set()
    for minutes in range(1, 6):
        end_borders.add(add_delta(end, minutes))

    ans = []
    curr = start
    while curr not in end_borders:
        ans.append(int(curr))
        curr = add_delta(curr, 5)

    print(ans)


def clean_time(t, days, is_end=False):
    t = t.split()
    day = days[t[0]]
    hrs_mins = t[1].split(':')
    hrs = int(hrs_mins[0])
    mins = int(hrs_mins[1])

    if t[2] == 'pm':
        if hrs < 12:
            hrs += 1
    else:
        if hrs == 12:
            hrs = 0

    nearest = mins % 5
    if nearest < 3:
        mins -= nearest
    else:
        if not is_end:
            return add_delta(
                str(day) + get_str(hrs) + get_str(mins), 5 - nearest
            )

    return str(day) + get_str(hrs) + get_str(mins)


def add_delta(t, delta_mins):
    day = int(t[0])
    hrs = int(t[1:3])
    mins = int(t[3:])

    if mins + delta_mins < 60:
        mins += delta_mins
        return str(day) + get_str(hrs) + get_str(mins)
    else:
        mins = 0
        if hrs + 1 < 24:
            hrs += 1
            return str(day) + get_str(hrs) + get_str(mins)
        else:
            hrs = 0
            if day + 1 < 8:
                day += 1
                return str(day) + get_str(hrs) + get_str(mins)
            else:
                day = 1
                return str(day) + get_str(hrs) + get_str(mins)


def get_str(i):
    if i < 10:
        return '0' + str(i)
    return str(i)



if __name__ == '__main__':
    times = ['tue 00:29 am', 'mon 11:56 pm']
    get_increments(times)
