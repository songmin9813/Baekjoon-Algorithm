import sys
t=int(sys.stdin.readline())
for _ in range(t):
    day=int(sys.stdin.readline())
    infos=list(map(int,sys.stdin.readline().split()))
    result=0
    max=infos[-1]
    for i in range(day-2,-1,-1):
        if infos[i] > max:
            max=infos[i]
        else:
            result+=max-infos[i]
    print(result)
    # 주식 사기의 기본 : 현재 시점에서 가장 비싸게 팔 수 있는 미래에서 판매
    # 이를 거꾸로 생각해보면 **뒤에서 가장 큰 값 아래로 발생하는 모든 값들은 수익으로 변환될 수 있음**
    # 따라서 현재의 max값을 뒤에서 유지하면서 계속 result를 누적하거나 max를 갱신하거나 둘 중에 하나만 해도 됨