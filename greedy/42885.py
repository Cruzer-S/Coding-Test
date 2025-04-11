def solution(people, limit):
    answer = 0

    people = sorted(people)

    min = 0
    max = -1
    while (len(people) - min + (max + 1)) > 1:
        if people[min] + people[max] > limit:
            max -= 1
        else:
            min += 1
            max -= 1

        answer += 1

    if len(people) != (min - (max + 1)):
        answer += 1

    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([100], 100))
print(solution([60], 100))
