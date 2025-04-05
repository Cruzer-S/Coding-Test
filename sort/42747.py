def solution(citations):
    citations = sorted(citations)

    nhigh = len(citations)
    npaper = 0
    index = nhigh - 1

    while index >= 0:
        if citations[index] < nhigh:
            nhigh = citations[index]

        npaper += 1

        if index > 0:
            if citations[index - 1] < nhigh:
                if citations[index - 1] < npaper:
                    break

        index -= 1

    return npaper if nhigh > npaper else nhigh

print(solution([1, 2]))
print(solution([2]))
print(solution([3, 0 ,6 ,1 ,5]))
print(solution([0]))
print(solution([0, 1, 2]))
print(solution([1000, 1, 1000]))
print(solution([1000,5,1000,5]))
print(solution([1000,6,1000,5,4,4]))
print(solution([1000,6,1000,5,4,5]))
