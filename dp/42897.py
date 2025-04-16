def calc(money):
    table = [ 0 for _ in range(len(money)) ]

    table[0] = money[0]
    table[1] = max(table[0], money[1])

    for i in range(2, len(money)):
        m1 = table[i - 2] + money[i]
        m2 = table[i - 1]

        if m1 > m2:
            table[i] = m1
        else:
            table[i] = m2

    return table[-1]

def solution(money):
    money1 = list.copy(money)
    money1[0] = 0

    money2 = list.copy(money)
    money2[-1] = 0

    m1 = calc(money1)
    m2 = calc(money2)

    return m1 if m1 > m2 else m2

print(solution([1, 2, 3, 1]))
print(solution([11, 10, 7]))
print(solution([1, 2, 3]))
print(solution([2, 1, 3]))
print(solution([2, 3, 1]))
print(solution([3, 2, 1]))
print(solution([3, 1, 2]))
print(solution([10, 5, 3, 1, 10]))
print(solution([0, 0, 2, 1, 0, 0, 1]))
