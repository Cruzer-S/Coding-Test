def calc_tower(tid, wires) -> int:
    node = None

    idx = 0 
    while idx < len(wires):
        if wires[idx][0] == tid:
            node = wires.pop(idx)
            break
        elif wires[idx][1] == tid:
            node = wires.pop(idx)
            break

        idx += 1

    if node is None:
        return 1

    return calc_tower(node[0], wires) + calc_tower(node[1], wires)

def solution(n, wires):
    answer = n + 1

    i = 0
    while i < len(wires):
        if i + 1 < len(wires):
            wire = wires[:i] + wires[i + 1:]
        else:
            wire = wires[:-1]

        t1 = calc_tower(wires[i][0], list.copy(wire))
        t2 = calc_tower(wires[i][1], list.copy(wire))

        if (abs(t1 - t2) < answer):
            answer = abs(t1 - t2)

        i += 1

    return answer

print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
