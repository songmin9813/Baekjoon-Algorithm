import sys
sys.setrecursionlimit(100000)
#별찍기 문제는 배열을 선언하여 조절할 것
def tracking(x1,x2,y1,y2):
    if x2-x1==3:
        global result
        count=0
        for i1 in range(x1,x2):
            for i2 in range(y1,y2):
                if count==4:
                    result[i1][i2]=' '
                else:
                    result[i1][i2]='*'
                count+=1
        return
    xlength,ylength=(x2-x1)//3,(y2-y1)//3
    tracking(x1,x1+xlength,y1,y1+ylength)
    tracking(x1,x1+xlength,y1+ylength,y1+ylength*2)
    tracking(x1,x1+xlength,y1+ylength*2,y2)

    tracking(x1+xlength,x1+xlength*2,y1,y1+ylength)
    tracking(x1+xlength,x1+xlength*2,y1+ylength*2,y2)

    tracking(x1+xlength*2,x2,y1,y1+ylength)
    tracking(x1+xlength*2,x2,y1+ylength,y1+ylength*2)
    tracking(x1+xlength*2,x2,y1+ylength*2,y2)
n=int(sys.stdin.readline())
result=[[' ' for _ in range(n)]for _ in range(n)]
tracking(0,n,0,n)
for i1 in range(n):
    print("".join(result[i1]))