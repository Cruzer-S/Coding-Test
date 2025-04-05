def solution(answers):
    answer = []
    
    highest = -1

    pattern = [[0, 0, [1, 2, 3, 4, 5]],
               [0, 0, [2, 1, 2, 3, 2, 4, 2, 5]],
               [0, 0, [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]]

    for ans in answers:
        for pat in pattern:
            s, i, p = pat

            if (p[i] == ans):
                s += 1

                if (s > highest):
                    highest = s

            pat[0] = s
            pat[1] = (i + 1) % len(pat[2])

    i = 0
    while i < len(pattern):
        if (pattern[i][0] >= highest):
            answer.append(i + 1)

        i += 1

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
