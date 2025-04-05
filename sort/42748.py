def solution(array, commands):
    answer = list()

    for cmd in commands:
        arr = array[cmd[0] - 1:cmd[1]]

        arr = sorted(arr)

        answer.append(arr[cmd[2] - 1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
