def solution(n, losts, reserves):
    answer = 0

    losts = sorted(losts)
    reserves = sorted(reserves)

    answer = n - len(losts)

    i = 0
    while i < len(losts):
        if losts[i] in reserves:
            reserves.remove(losts[i])
            losts.remove(losts[i])

            answer += 1

            continue

        i += 1

    while len(losts) > 0:
        lost = losts.pop(0)

        while len(reserves) > 0:
            if (reserves[0] > lost + 1):
                break

            reserve = reserves.pop(0)
            if (abs(reserve - lost) == 1):
                answer += 1
                break
        
    return answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
print(solution(5, [1, 2, 5], [2, 3]))
print(solution(5, [1, 2, 4], [2, 3]))
