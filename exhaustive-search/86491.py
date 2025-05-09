def solution(sizes):
    minw = -1
    minh = -1

    for size in sizes:
        if size[0] < size[1]:
            temp = size[1]
            size[1] = size[0]
            size[0] = temp

        if size[0] > minw:
            minw = size[0]

        if size[1] > minh:
            minh = size[1]

    return minw * minh

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))
