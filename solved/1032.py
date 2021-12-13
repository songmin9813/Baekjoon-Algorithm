n=int(input())
string=list(input())
for _ in range(n-1):
    others=list(input())
    for i,al in enumerate(string):
        if string[i]=='?':
            continue
        if string[i]!=others[i]:
            string[i]='?'
print(''.join(string))