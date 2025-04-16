def goto(x, y, max_x, max_y, puddle, way):
    count = 0

    if x == (max_x - 1) and y == (max_y - 1):
        return 1

    if puddle[y][x] == 1:
        return 0

    if x + 1 < max_x:
        if way[y][x + 1] == -1:
            way[y][x + 1] = goto(x + 1, y, max_x, max_y, puddle, way)

        count += way[y][x + 1]

    if y + 1 < max_y:
        if way[y + 1][x] == -1:
            way[y + 1][x] = goto(x, y + 1, max_x, max_y, puddle, way)

        count += way[y + 1][x]

    return count

def solution(max_x, max_y, puddles):
    puddle_table = [ [ 0 for x in range(max_x) ] for y in range(max_y) ]
    way_table = [ [ -1 for x in range(max_x)] for y in range(max_y) ]

    for puddle in puddles:
        x, y = puddle[0] - 1, puddle[1] - 1
        puddle_table[y][x] = 1

    return goto(0, 0, max_x, max_y, puddle_table, way_table) % 1000000007

print(solution(4, 3, [[2, 2]]))
print(solution(5, 5, []))
