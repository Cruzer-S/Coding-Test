def solution(begin, target, words):
    queue = list()

    queue.append([begin, 0, []])

    while len(queue) > 0:
        word, n, using = queue.pop(0)

        if word == target:
            return n

        for w in words:
            if w in using:
                continue

            diff = 0
            for i in range(len(w)):
                if word[i] != w[i]:
                    diff += 1

                if diff > 1:
                    break

            if diff > 1:
                continue

            queue.append([w, n + 1, using + [w]])

    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
