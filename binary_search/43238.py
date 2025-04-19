def solution(n, times):
    times = sorted(times)

    start = (n // len(times)) * times[0]
    end = times[-1] * n

    while start <= end:
        x = 0

        mid = (start + end) // 2
        for time in times:
            x += mid // time 

        if x >= n:
            end = mid - 1

            xp = 0
            for time in times:
                xp += (mid - 1) // time

            if xp < n:
                return mid

            mid = (start + mid) // 2

        if x < n:
            start = mid + 1

    pass

print(solution(6, [7, 10]))
print(solution(5, [3, 5, 7]))
print(solution(8, [1, 3, 5 ,7]))
