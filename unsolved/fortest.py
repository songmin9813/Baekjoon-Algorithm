import sys

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(19)]

# 좌 & 우, 상 & 하, 우대각선, 좌대각선

dx = [0,1,1,1]
dy = [1,0,1,-1]

def dfs(x,y,d,k):

    if x < 0 or x >= 19 or y < 0 or y >= 19 :
        return False

    if visited[x][y] == False and graph[x][y] == d : 
        doll_list.append([d,x,y])
        visited[x][y] = True
        nx = x + dx[k]
        ny = y + dy[k]
        dfs(nx,ny,d,k)
        return True
    return False

black,white = [],[]

for d in range(1,3):
    for j in range(19):
        for i in range(19):
            for k in range(4):
                visited = [[False]*19 for _ in range(19)] 
                doll_list = []
                if dfs(i,j,d,k) == True:
                    if len(doll_list) == 5 :
                        # 육목 확인
                        if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 and graph[i - dx[k]][j - dy[k]] != d:
                            if d == 1 :
                                black.append(doll_list)
                            elif d == 2 :
                                white.append(doll_list)
if len(black)>len(white):
    black = sorted(black[0], key = lambda x : (x[2],x[1]))
    print(1)
    print(black[0][1]+1,black[0][2]+1)
elif len(black)<len(white):
    white = sorted(white[0], key = lambda x : (x[2],x[1]))
    print(2)
    print(white[0][1]+1,white[0][2]+1)
elif len(black) == len(white):
    print(0)