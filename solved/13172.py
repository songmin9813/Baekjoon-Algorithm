import sys
#임영센세...그는...빛...
def gcd(a,b):
    if a<b:
        tmp=a
        a=b
        b=tmp
    while b!=0:
        n=a%b
        a=b
        b=n
    return a
def inverse(a,b):
    board=[]
    while True:
        board.append([a,a//b,b,a%b])
        if a%b==1:
            break
        tmp=a%b
        a=b
        b=tmp
    a,b,c,d=1,board[-1][0],-board[-1][1],board[-1][2]
    for i in range(len(board)-2,-1,-1):
        newa,newb=c,board[i][0]
        newc,newd=(1-newa*newb)//board[i][2],board[i][2]
        a,b,c,d=newa,newb,newc,newd
    return c
n=int(sys.stdin.readline())
board=[]
for _ in range(n):
    one,two=map(int,sys.stdin.readline().split())
    if not board:
        board.append(one)
        board.append(two)
    else:
        lcd=one*board[0]//gcd(one,board[0])
        tmp=lcd//one*two
        board[1]=lcd//board[0]*board[1]+tmp
        board[0]=lcd
a,b=board[1],board[0]
binver=inverse(1000000007,b)
print(a*binver%1000000007)