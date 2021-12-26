import sys
def checking(board,x,y):
    global result
    blueX=[[x,x,x,x],[x,x+1,x+2,x+3]]
    blueY=[[y,y+1,y+2,y+3],[y,y,y,y]]#일자모양좌표
    yellowX=[[x,x,x+1,x+1]]
    yellowY=[[y,y+1,y,y+1]]#네모모양좌표
    orangeX=[[x,x,x-1,x-2],[x,x-1,x-1,x-1],[x,x,x+1,x+2],[x,x+1,x+1,x+1],[x,x,x-1,x-2],[x,x+1,x+1,x+1],[x,x,x+1,x+2],[x,x-1,x-1,x-1]]
    orangeY=[[y,y-1,y-1,y-1],[y,y,y+1,y+1],[y,y+1,y+1,y+1],[y,y,y-1,y-2],[y,y+1,y+1,y+1],[y,y,y+1,y+1],[y,y-1,y-1,y-1],[y,y,y-1,y-2]]#이상한니은좌표
    
n,m=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result=0