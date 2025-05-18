import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while scoville[0] < K and len(scoville) >= 2:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        count += 1
    
    if scoville[0] >= K:
        return count
    else:
        return -1