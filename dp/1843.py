def calc(start, end, operation, table):
    largest = None
    smallest = None

    if table[start][end] is not None:
        return table[start][end]

    if start == end:
        table[start][end] = [int(operation[start]), int(operation[end])]
        return table[start][end]

    for i in range(start, end, 2):
        result = list()

        left = calc(start, i, operation, table)
        operator = operation[i + 1]
        right = calc(i + 2, end, operation, table)

        if operator == '+':
            result.append(left[0] + right[0])
            result.append(left[0] + right[1])
            result.append(left[1] + right[0])
            result.append(left[1] + right[1])
        elif operator == '-':
            result.append(left[0] - right[0])
            result.append(left[0] - right[1])
            result.append(left[1] - right[0])
            result.append(left[1] - right[1])

        result = sorted(result)

        if smallest is None:
            smallest = result[0]

        if largest is None:
            largest = result[3]

        if result[0] < smallest:
            smallest = result[0]

        if result[3] > largest:
            largest = result[3]

    table[start][end] = [smallest, largest]

    return table[start][end]


def solution(arr):
    table = [
            [ None for j in range(len(arr)) ]
        for i in range(len(arr))
    ]

    return calc(0, len(arr) - 1, arr, table)[1]
