def solution(clothes):
    parts = dict()
    answer = 1

    for cloth in clothes:
        if cloth[1] in parts:
            parts[cloth[1]] += 1
        else:
            parts[cloth[1]] = 1

    for v in parts.values():
        answer *= (v + 1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
