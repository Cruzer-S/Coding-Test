import heapq as hp

class job:
    def __init__(self, number, req_time, run_time):
        self.number = number
        self.req_time = req_time
        self.run_time = run_time

    def __lt__(self, other):
        if (self.run_time < other.run_time):
            return True
        elif (self.run_time == other.run_time):
            if (self.req_time < other.req_time):
                return True
            elif (self.req_time == other.req_time):
                return self.number < other.number

        return False

    def __str__(self):
        return "{ %d, %d, %d }" % (self.number, self.req_time, self.run_time)

def solution(jobs):
    cur_time = 0
    ta_time = 0
    job_queue = list()
    time_queue = list()

    for i in range(len(jobs)):
        time_queue.append(job(i, jobs[i][0], jobs[i][1]))
    
    hp.heapify(job_queue)
    time_queue = sorted(time_queue, key = lambda j: j.req_time)

    while len(time_queue) > 0:
        while (time_queue[0].req_time <= cur_time):
            p = time_queue.pop(0)
            hp.heappush(job_queue, p)

            if (len(time_queue) <= 0):
                break

        if (len(job_queue) == 0):
            cur_time = time_queue[0].req_time
            continue

        j = hp.heappop(job_queue)

        cur_time += j.run_time
        ta_time += cur_time - j.req_time

    while len(job_queue) > 0:
        j = hp.heappop(job_queue)

        cur_time += j.run_time
        ta_time += cur_time - j.req_time

    return ta_time // len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))
print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))
print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))
print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))
print(solution([[0, 10]]))
