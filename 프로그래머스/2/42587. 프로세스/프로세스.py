import collections

def solution(priorities, location):
    answer = 0
    
    q = collections.deque()
    for i, p in enumerate(priorities):
        q.append((p, i))

    while q:
        current = q.popleft() 
        flag = False
        for p, i in q:
            if p > current[0]:
                flag = True
                break
        
        if flag:
            q.append(current)
        else:
            answer += 1 

            if current[1] == location:
                return answer

    return answer
