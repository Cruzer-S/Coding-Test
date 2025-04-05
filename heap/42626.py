import heapq as hp

def solution(scoville, K):
    hp.heapify(scoville)

    times = 0

    if (scoville[0] >= K):
        return times

    while len(scoville) >= 2:
        n1 = hp.heappop(scoville)
        n2 = hp.heappop(scoville)

        sco = n1 + n2 * 2

        hp.heappush(scoville, sco)

        times += 1

        if (K <= scoville[0]):
            return times

    if (K <= scoville[0]):
            return times

    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2], 7))
