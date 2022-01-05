import sys
n=int(sys.stdin.readline())
#6의 배수에서는 양 끝단에서만 퍼진다
base=5*(n//3)+(n//3-1)#가장 아래 최대 띄어쓰기
line=[' ' for _ in range(base)]
newline=[' ' for _ in range(base)]
line[len(line)//2]='*'
print(''.join(line))
for i in range(1,n):
    if i%3==0:#점 하나 찍기. 덩어리별 양 끝단 계산 필요
        sets,svpoint=-1,-1#set=-1:초기상태, set=0:덩어리 진행중, set=1:띄어쓰기를 한 번 만남
        for i1,value in enumerate(line):
            if value=='*':#별모양
                if sets==-1:#덩어리의 처음을 만남
                    svpoint=i1
                    sets=0
                elif sets==1:#아직 덩어리임
                    sets=0
                else:
                    continue
            else:#띄어쓰기
                if sets==0:#띄어쓰기는 한번까지 허용
                    sets+=1
                elif sets==1:#그이상은 덩어리 취급이 안 됨
                    sets=-1
                    newline[svpoint-1]='*'
                    newline[i1-1]='*'
                    svpoint=i1
                else:
                    continue
    elif i%3==1:#점이 두개로 나뉨 
        for i1,value in enumerate(line):
            if value=='*':
                newline[i1-1]='*'
                newline[i1+1]='*'
    else:#점 다섯개 찍음
        count,svpoint=0,-1
        for i1,value in enumerate(line):
            if value=='*':
                if count==0:
                    count+=1
                    svpoint=i1
                else:
                    count=0
                    for i2 in range(svpoint-1,i1+2):
                        newline[i2]='*'
                    svpoint=-1
    print(''.join(newline))
    line=newline.copy()
    newline=[' ' for _ in range(base)]