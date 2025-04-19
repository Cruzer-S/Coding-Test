def shortest_path(maps):
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    queue = list()

    queue.append(([0, 0], 1))

    while len(queue) > 0:
        position, walk = queue.pop(0)

        x = position[0]
        y = position[1]

        if (x < 0 or y < 0) or (x >= len(maps[0]) or y >= len(maps)):
            continue

        if maps[y][x] == 0:
            continue

        if position == [len(maps[0]) - 1, len(maps) - 1]:
            return walk

        if maps[y][x] != 1:
            continue

        if maps[y][x] != 1 and maps[y][x] < walk:
            continue

        maps[y][x] = walk

        for d in direction:
            queue.append(([position[0] + d[0], position[1] + d[1]], walk + 1))

    return -1

def solution(maps):
    n = shortest_path(maps)

    return n

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
print(solution([[1, 1]]))
