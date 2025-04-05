from itertools import permutations

def is_prime(number):
    i = 2

    if number < 2:
        return False

    while (i * i) <= number:
        if number % i == 0:
            return False

        i += 1

    return True

def solution(numbers):
    num_list = []
    answer = 0

    for i in range(len(numbers)):
        for nums in permutations(numbers, i + 1):
            num_list.append(int(''.join(nums)))

    num_list = set(num_list)

    for num in num_list:
        if is_prime(num):
            answer += 1

    return answer

print(solution("2221"))
