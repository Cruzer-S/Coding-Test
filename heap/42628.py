import heapq

def solution(operations):
    minheap = []
    maxheap = []

    for ops in operations:
        op = ops[0]
        num = int(ops[1:])

        if op == 'I':
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
        else:
            if num == -1:
                if (len(minheap) == 0):
                    continue

                v = heapq.heappop(minheap)
                if -v in maxheap:
                    maxheap.remove(-v)
            else:
                if (len(maxheap) == 0):
                    continue

                v = heapq.heappop(maxheap)
                if -v in minheap:
                    minheap.remove(-v)

    if len(minheap) == 0:
        return [0, 0]
    else:
        return [max(minheap), min(minheap)]
