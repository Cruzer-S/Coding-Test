from functools import cmp_to_key

def comp(n1, n2):
    n1 = str(n1)
    n2 = str(n2)

    swap = n2 + n1
    noswap = n1 + n2

    if (swap == noswap):
        return 0

    return -1 if swap < noswap else +1

def solution(numbers):
    answer = ''

    numbers = sorted(numbers, key = cmp_to_key(comp))

    while len(numbers) > 0:
        answer += str(numbers.pop(0))

    while len(answer) > 1:
        if answer[0] != '0':
            break

        answer = answer[1:]

    return answer

print(solution([32, 3, 34, 3, 30, 300]))
