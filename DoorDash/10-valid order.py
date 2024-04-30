# given an pickup delivery, return whether it is valid or not

def validate(pattern):
    picked_up = set()
    delivered = set()

    for task in pattern:
        task_type = task[0]
        task_id = task[1:]
        if task_type == 'P':
            if task_id not in picked_up:
                picked_up.add(task_id)
            else:
                return False
        else:
            if task_id not in delivered and task_id in picked_up:
                delivered.add(task_id)
            else:
                return False


    return len(picked_up) == len(delivered)


if __name__ == '__main__':
    pattern = [
        'P1', 'P3', 'P2', 'D3', 'P4', 'P404', 'D2', 'D1', 'D404', 'D4',
        'P33', 'D33',
    ]

    print(validate(pattern))
