def solution(nums):
    poke = dict()

    for n in nums:
        if n in poke:
            poke[n] += 1
        else:
            poke[n] = 1

    if len(poke.keys()) > len(nums) / 2:
        return int(len(nums) / 2)
    else:
        return int(len(poke.keys()))

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
