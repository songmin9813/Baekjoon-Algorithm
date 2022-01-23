import sys
import itertools
tc=int(sys.stdin.readline())
for _ in range(tc):
    n=int(sys.stdin.readline())
    points=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
    result=2<<30
    combi=itertools.combinations(range(0,n),n//2)
    for tu in combi:
        visited={i:True for i in range(n)}
        x,y=0,0
        for index in tu:
            x+=points[index][0]
            y+=points[index][1]
            del visited[index]
        for index in visited.keys():
            x-=points[index][0]
            y-=points[index][1]
        result=min(result, (x*x+y*y)**0.5)
    print(result)