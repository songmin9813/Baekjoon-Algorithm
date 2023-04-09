import sys
def dfs(T):
    if len(S)==len(T):
           return S==T
    if T[0]=='B' and dfs(T[:0:-1]): # 슬라이싱 step 끝난 이후 끝자리는 절삭됨에 유의
            return 1
    if T[-1]=='A' and dfs(T[:-1]):
            return 1
    return 0
S=sys.stdin.readline().rstrip()
T=sys.stdin.readline().rstrip()
print(dfs(T))