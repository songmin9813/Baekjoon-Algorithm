def tracking(board):
    global output
    tmpresult=judge(board)
    if tmpresult!=2:
        output[tmpresult+1]+=1
        return
    else:
        new_board=[]
        row=board[:len(board)//3]
        for value in row:
            new_board.append(value[:len(value)//3])
        tracking(new_board)
        
        new_board=[]
        row=board[:len(board)//3]
        for value in row:
            new_board.append(value[len(value)//3:len(value)//3*2])
        tracking(new_board)
        
        new_board=[]
        row=board[:len(board)//3]
        for value in row:
            new_board.append(value[len(value)//3*2:])
        tracking(new_board)
        
        new_board=[]
        row=board[len(board)//3:len(board)//3*2]
        for value in row:
            new_board.append(value[:len(value)//3])
        tracking(new_board)
        
        new_board=[]
        row=board[len(board)//3:len(board)//3*2]
        for value in row:
            new_board.append(value[len(value)//3:len(value)//3*2])
        tracking(new_board)
        
        new_board=[]
        row=board[len(board)//3:len(board)//3*2]
        for value in row:
            new_board.append(value[len(value)//3*2:])
        tracking(new_board)
        
        new_board=[]
        row=board[len(board)//3*2:]
        for value in row:
            new_board.append(value[:len(value)//3])
        tracking(new_board)
        
        new_board=[]
        row=board[len(board)//3*2:]
        for value in row:
            new_board.append(value[len(value)//3:len(value)//3*2])
        tracking(new_board)
        
        new_board=[]
        row=board[len(board)//3*2:]
        for value in row:
            new_board.append(value[len(value)//3*2:])
        tracking(new_board)
def judge(board):
    result=board[0][0]
    for i,row in enumerate(board):
        for i1,value in enumerate(row):
            if i==0 and i1==0:
                continue
            if value!=result:
                return 2
    return result
            
output=[0,0,0]
n=int(input())
board=[list(map(int,input().split())) for _ in range(n)]
tracking(board)
print(str(output[0])+'\n'+str(output[1])+'\n'+str(output[2]))
