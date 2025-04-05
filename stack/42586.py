def solution(progresses, speeds):
    answer = []

    idx = 0
    while idx < len(progresses):
        for i in range(len(progresses[idx:])):
            progresses[idx + i] += speeds[idx + i]

        prev = idx
        while progresses[idx] >= 100:
            idx += 1

            if (idx >= len(progresses)):
                break

        if (prev == idx):
            continue

        answer.append(idx - prev)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
