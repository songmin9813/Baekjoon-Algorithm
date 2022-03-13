import sys
import heapq
#처음에 dp로 풀려고 해서 틀림
#접근은 좋았으나 dp의 단방향 특성을 위배하기 때문에 dp로 풀 수 없음
#애초에 dp로 생각한 이유 : 각 위치에 대한 최적 경로를 찾아내는 방식으로 탐색해보자
#각 위치에 대한 최소 경로는 다익스트라 알고리즘을 사용하도록 하자
def dijk():
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=[]
    dist=[[2<<30 for _ in range(n)]for _ in range(n)]
    dist[0][0]=board[0][0]
    heapq.heappush(queue,[dist[0][0],0,0])
    while queue:
        cdist,cx,cy=heapq.heappop(queue)
        if cdist>dist[cx][cy]:
            continue
        for i in range(4):
            newX=cx+dx[i]
            newY=cy+dy[i]
            if 0<=newX<n and 0<=newY<n:
                newdist=cdist+board[newX][newY]
                if newdist<dist[newX][newY]:
                    dist[newX][newY]=newdist
                    heapq.heappush(queue,[dist[newX][newY],newX,newY])
    return dist
n=int(sys.stdin.readline())
board=[list(sys.stdin.readline().rstrip()) for _ in range(n)]
for i1,row in enumerate(board):
    for i2,value in enumerate(row):
        if value=='0':
            board[i1][i2]=1
        else:
            board[i1][i2]=0
result=dijk()
print(result[n-1][n-1])