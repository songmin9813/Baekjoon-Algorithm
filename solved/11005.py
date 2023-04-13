import sys
n,b=map(int, sys.stdin.readline().split())
result=[]
codes=[chr(value) for value in range(ord("0"),ord("9")+1)]+[chr(value) for value in range(ord("A"),ord("Z")+1)]
while n>=b:
    result.append(codes[n%b])
    n=n//b
result.append(codes[n])
result.reverse()
print("".join(result))