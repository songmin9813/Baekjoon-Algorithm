import sys
import heapq
from collections import Counter
n=int(sys.stdin.readline())
list_=[]
for _ in range(n):
    list_.append(int(sys.stdin.readline()))
list_.sort()
avr=sum(list_)/n
if avr>=0:
    avr=int(avr) if avr-int(avr)<0.5 else int(avr)+1
else:
    avr=int(avr) if avr-int(avr)>-0.5 else int(avr)-1
print(avr)
print(list_[n//2])
count=Counter(list_)
maxcount=max(count.values())
countlist=[]
for k,v in count.items():
    if maxcount==v:
        heapq.heappush(countlist,k)
if len(countlist)==1:
    print(countlist[0])
else:
    heapq.heappop(countlist)
    print(countlist[0])
print(list_[-1]-list_[0])