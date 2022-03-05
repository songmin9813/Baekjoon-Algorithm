from collections import deque
def solution(number,target):
    result=0
    queue=deque()
    queue.append(-number[0])
    queue.append(number[0])
    for i in range(1,len(number)):
        l=len(queue)
        for _ in range(l):
            cv=queue.popleft()
            minus,plus=cv-number[i],cv+number[i]
            if i==len(number)-1:
                if minus==target:
                    result+=1
                if plus==target:
                    result+=1
            queue.append(cv+number[i])
            queue.append(cv-number[i])
    return result