def solution(priorities, location):
    prio_list = list()
    run = 1

    for i in range(len(priorities)):
        prio_list.append((i, priorities[i]))

    while True:
        highest = 0

        for i in range(len(prio_list)):
            if prio_list[i][1] > highest:
                highest = prio_list[i][1]

        while True:
            i, p = prio_list.pop(0)

            if (p >= highest):
                if (i == location):
                    return run
                run += 1
                break

            prio_list.append((i, p))

    return None 

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
