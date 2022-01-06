import sys
string=sys.stdin.readline().rstrip()
obj=list(sys.stdin.readline().rstrip())
stack=[]
for i,v in enumerate(string):
    stack.append(v)
    if stack[-len(obj):]==obj:
        stack[-len(obj):]=[]
print(''.join(stack)) if stack else print('FRULA')