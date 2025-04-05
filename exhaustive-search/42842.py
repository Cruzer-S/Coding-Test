def solution(brown, yellow):
    for width in range(0, yellow):
        width = width + 1
        height = yellow // width

        if (width * height != yellow):
            continue

        bwidth = width + 2
        bheight = height + 2

        if (bwidth * bheight == (brown + yellow)):
            if (bwidth < bheight):
                return [bheight, bwidth]
            else:
                return [bwidth, bheight]

    return None

print(solution(10, 2))
print(solution(24, 24))
print(solution(8, 1))
