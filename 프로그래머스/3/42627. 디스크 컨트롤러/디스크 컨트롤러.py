import heapq

def solution(jobs):
    jobs.sort()
    heap = []
    time, total, idx, count = 0, 0, 0, 0
    n = len(jobs)

    while count < n:
        while idx < n and jobs[idx][0] <= time:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1

        if heap:
            duration, start = heapq.heappop(heap)
            time += duration
            total += (time - start)
            count += 1
        else:
            time = jobs[idx][0]

    return total // n
