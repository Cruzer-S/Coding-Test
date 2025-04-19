def get_link(computer, computers, link):
    link.append(computer)

    for i in range(len(computers[computer])):
        if i == computer:
            continue

        if i in link:
            continue

        if computers[computer][i] == 1:
            computers[i][computer] = 0
            get_link(i, computers, link)

    return link

def solution(n, computers):
    unlinked = [ i for i in range(len(computers)) ]
    answer = 0

    while len(unlinked) > 0:
        linked = get_link(unlinked[0], computers, [])

        for link in linked:
            unlinked.remove(link)

        print(linked)

        answer += 1

    return answer

print(solution(9, [
    [1, 1, 1, 1, 0, 0, 0, 0, 0], # 1: 1 - 2 - 3 - 4
    [1, 1, 0, 0, 0, 0, 0, 0, 0], # 2: 1 - 2
    [1, 0, 1, 0, 1, 0, 0, 0, 0], # 3: 1 - 3 - 5
    [1, 0, 0, 1, 1, 0, 0, 0, 0], # 4: 1 - 4 - 5
    [0, 0, 1, 1, 1, 0, 0, 0, 0], # 5: 3 - 4 - 5
    [0, 0, 0, 0, 0, 1, 0, 0, 0], # 6: 6
    [0, 0, 0, 0, 0, 0, 1, 0, 0], # 7: 7
    [0, 0, 0, 0, 0, 0, 0, 1, 1], # 8: 8 - 9
    [0, 0, 0, 0, 0, 0, 0, 1, 1], # 9: 8 - 9
]))
