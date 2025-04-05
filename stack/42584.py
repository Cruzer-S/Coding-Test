def solution(prices):
    answer = []

    for _ in prices:
        answer.append(0)

    i = 0
    while i < len(answer):
        j = i + 1

        while j < len(prices):
            answer[i] += 1
            if (prices[i] > prices[j]):
                break

            j += 1

        i += 1

    return answer

print(solution([1, 2, 3, 2, 3]))
