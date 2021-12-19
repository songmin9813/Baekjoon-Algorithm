def tracking(board):
    global result
    tmpresult=judge(board)
    if tmpresult!=2:
        result+=str(tmpresult)
        return
    else:
        result+='('
        tmp=board[:len(board)//2]
        new_board=[]
        for row in tmp:
            new_board.append(row[:len(row)//2])
        tracking(new_board)
        
        tmp=board[:len(board)//2]
        new_board=[]
        for row in tmp:
            new_board.append(row[len(row)//2:])
        tracking(new_board)
        
        tmp=board[len(board)//2:]
        new_board=[]
        for row in tmp:
            new_board.append(row[:len(row)//2])
        tracking(new_board)
        
        tmp=board[len(board)//2:]
        new_board=[]
        for row in tmp:
            new_board.append(row[len(row)//2:])
        tracking(new_board)
        result+=')'
        
def judge(board):
    result=board[0][0]
    for row in board:
        for value in row:
            if result!=value:
                return 2
    return result

n=int(input())
board=[list(map(int,input())) for _ in range(n)]
result=''
tracking(board)
print(result)