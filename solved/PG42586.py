from collections import deque
def solution(progresses, speeds):
    queue=deque()
    result=[]
    for i in range(len(progresses)):
        queue.append([progresses[i],speeds[i]])
    while queue:
        count,l=0,len(queue)
        for tmp in range(l):
            cv=queue.popleft()
            cv[0]+=cv[1]
            if cv[0]>=100 and tmp==count:
                count+=1
            else:
                queue.append(cv)
        if count!=0:
            result.append(count)
    return result