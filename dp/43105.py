def solution(triangle):
    while len(triangle) > 1:
        last = len(triangle) - 2

        for i in range(last + 1):
            left = triangle[last + 1][i]
            right = triangle[last + 1][i + 1]

            if left < right:
                triangle[last][i] += right
            else:
                triangle[last][i] += left 

        triangle = triangle[:-1]

    return triangle[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
