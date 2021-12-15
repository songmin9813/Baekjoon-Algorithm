def divide(board):#counts[0]이 하얀색
    if len(board)==1:
        if board[0][0]==0:
            counts[0]+=1
        else:
            counts[1]+=1
        return
    if checking(board):
        counts[board[0][0]]+=1
    else:
        new_board=[]
        for row in board[:len(board)//2]:
            new_board.append(row[:len(board)//2])
        divide(new_board)
        new_board=[]
        for row in board[:len(board)//2]:
            new_board.append(row[len(board)//2:])
        divide(new_board)
        new_board=[]
        for row in board[len(board)//2:]:
            new_board.append(row[len(board)//2:])
        divide(new_board)
        new_board=[]
        for row in board[len(board)//2:]:
            new_board.append(row[:len(board)//2])
        divide(new_board)
def checking(board):
    temp=board[0][0]
    for i,row in enumerate(board):
        for i1,value in enumerate(row):
            if i==0 and i1==0:
                continue
            if value!=temp:
                return False
    return True
n=int(input())
board=[]
counts=[0,0]
for _ in range(n):
    board.append(list(map(int,input().split())))
temp_=[[1,2,3,4],[3,4,4,6],[7,8,9,0],[1,2,3,4]]
print(temp_[:2][:2])
divide(board)
print(str(counts[0])+'\n'+str(counts[1]))