from pytest import importorskip


import sys
import heapq
def dijk(start):
    dist=[2<<30 for _ in range(n+1)]
    dist[start]=0
    queue=[[0,start]]#초기 시작 위치를 처음 큐에 할당하여야 함
    #nextNode를 초기에 넣는게 아님!!
    while queue:
        cd,cy=heapq.heappop(queue)
        if dist[cy]<cd:
            continue
        for nextNode in nodes[cy]:
            newdist=cd+nextNode[0]
            if dist[nextNode[1]]>newdist:
                dist[nextNode[1]]=newdist
                heapq.heappush(queue,[newdist,nextNode[1]])
    return dist

def counting():
    list_=[0,0]
    for i in range(1,n+1):
        if result[i]!=2<<30:
            list_[0]+=1
            list_[1]=max(list_[1],result[i])
    return list_
tc=int(sys.stdin.readline())
for _ in range(tc):
    n,d,c=map(int,sys.stdin.readline().split())
    nodes=[[]for _ in range(n+1)]
    for _ in range(d):
        y,x,d=map(int,sys.stdin.readline().split())
        nodes[x].append([d,y])
    result=dijk(c)
    counter=counting()
    print(counter[0],counter[1])