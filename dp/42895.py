def solution(N, number):
    combination = dict()
    operations = [
            lambda a, b: a + b,
            lambda a, b: a - b,
            lambda a, b: b - a,
            lambda a, b: a * b,
            lambda a, b: a // b,
            lambda a, b: b // a,
    ]

    for i in range(1, 6):
        result = int(str(N) * i)
        combination[int(str(N) * i)] = i

    for op in operations:
        result = op(N, N)
        if result < 1 or result > 32000:
            continue

        if result in combination:
            if combination[result] < 2:
                continue

        combination[op(N, N)] = 2

    for _ in range(0, 2):
        for op in operations:
            combi = list(combination.items())
            for i in range(0, len(combi)):
                for j in range(i, len(combi)):
                    num1, count1 = combi[i]
                    num2, count2 = combi[j]

                    if count1 + count2 > 8:
                        continue

                    result = op(num1, num2)
                    if result < 1 or result > 32000:
                        continue

                    count = count1 + count2

                    if result in combination:
                        if combination[result] < count:
                            continue

                    combination[result] = count

    return -1 if number not in combination else combination[number]
