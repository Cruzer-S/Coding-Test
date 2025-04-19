def find(numbers, target, current):
    if len(numbers) == 0:
        return 1 if target == current else 0

    return   find(numbers[1:], target, current - numbers[0])    \
           + find(numbers[1:], target, current + numbers[0])

def solution(numbers, target):
    return find(numbers, target, 0)

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))
