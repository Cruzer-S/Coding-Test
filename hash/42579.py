def solution(genres, plays):
    playtime = dict()
    genretop = dict()
    answer = list()

    for i in range(0, len(genres)):
        if genres[i] in playtime:
            playtime[genres[i]] += plays[i]
        else:
            playtime[genres[i]] = plays[i]

        if genres[i] in genretop:
            first_idx, second_idx = genretop[genres[i]]

            first = plays[first_idx]
            if (second_idx != -1):
                second = plays[second_idx]
            else:
                second = -1

            if (plays[i] > first):
                second_idx = first_idx
                first_idx = i
            elif (plays[i] > second):
                second_idx = i

            genretop[genres[i]] = (first_idx, second_idx)
        else:
            genretop[genres[i]] = (i, -1)

    playtime = dict(sorted(playtime.items(), key = lambda item: item[1], reverse = True))

    for genre in playtime.keys():
        first_idx, second_idx = genretop[genre]

        answer.append(first_idx)
        if (second_idx != -1):
            answer.append(second_idx)

    return answer

print(solution(["pop", "classic", "pop", "classic", "classic", "pop", "jazz"], [2500, 500, 600, 150, 800, 2500, 500]))
