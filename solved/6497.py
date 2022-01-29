
import sys
def find(x):
  if x!=root[x]:
    root[x]=find(root[x])
  return root[x]
def union(x,y,d):
  x=find(x)
  y=find(y)
  if x!=y:
    global result,count
    result+=d
    root[y]=x
    count+=1
while True:
  n,m=map(int,sys.stdin.readline().split())
  if n==0 and m==0:
    break
  edges=[list(map(int,sys.stdin.readline().split()))for _ in range(m)]
  result,count,sum=0,0,0
  root=[i for i in range(n)]
  for x,y,d in edges:
    sum+=d
  edges.sort(key=lambda x:x[2])
  for x,y,d in edges:
    union(x,y,d)
    if count==n-1:
      break
  print(sum-result)