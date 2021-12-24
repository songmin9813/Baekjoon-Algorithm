import copy
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
result=copy.deepcopy(board)#2차원 배열은 내부까지 copy가 안 됨
for i1 in range(n):
    visited=[False for _ in range(n)]
    stack=[]
    for i2 in range(n):
        if board[i1][i2]==1 and visited[i2] is not True:
            stack.append(i2)
            visited[i2]=True
            while len(stack)!=0:
                index=stack.pop()
                for i3 in range(n):
                    if board[index][i3]==1 and visited[i3] is not True:
                        visited[i3]=True
                        stack.append(i3)
                        result[i1][i3]=1
string=''
for row in result:
    for value in row:
        string+=str(value)+' '
    string+='\n'
print(string)