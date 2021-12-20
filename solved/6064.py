def numinvert(num, standard):#0이 아니라 기준값이 나오도록 짠 함수
    return num%standard if num%standard!=0 else standard
n=int(input())
for _ in range(n):
    m,n,x,y=map(int,input().split())
    result=x#x를 일단 맞춰준다음 진행함
    dy=numinvert(x,n)
    count=0
    while True:
        if dy==y:#y까지 적중한 케이스
            result+=count*m
            break
        dy=numinvert(dy+m, n)#x값을 y에 더해가면서 조건 검사함
        if numinvert(x,n)==dy:#처음값으로 되돌아옴-한 사이클동안 y를 찾지 못함-만들수없음
            result=-1
            break
        count+=1
    print(result)