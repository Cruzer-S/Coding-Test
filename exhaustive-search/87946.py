from itertools import permutations

def solution(k, dungeons):
    max = -1

    for dungeon_list in permutations(dungeons, len(dungeons)):
        exh = k
        ntimes = 0

        for dungeon in dungeon_list:
            if (dungeon[0] > exh):
                break

            ntimes += 1
            exh -= dungeon[1]

        if (ntimes > max):
            max = ntimes

    return max

print(solution(80, [[80, 20], [50, 40], [30, 10]]))
