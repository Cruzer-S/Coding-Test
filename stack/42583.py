def solution(max_length, max_weight, truck_weights):
    length = 0
    weight = 0

    in_bridge = list()

    time = 0

    while len(truck_weights) > 0 or len(in_bridge) != 0:
        time += 1

        i = 0
        while i < len(in_bridge):
            in_bridge[i] = (in_bridge[i][0] - 1, in_bridge[i][1])
            if (in_bridge[i][0] <= 0):
                weight -= in_bridge[i][1]
                length -= 1

                in_bridge.pop(0)
            else:
                i += 1

        if (len(truck_weights) == 0 and len(in_bridge) == 0):
            break

        if (len(truck_weights) > 0):
            if (weight + truck_weights[0] <= max_weight):
                if (length + 1 <= max_length):
                    weight += truck_weights[0]
                    length += 1

                    in_bridge.append((max_length, truck_weights[0]))
                    truck_weights.pop(0)

    return time

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
