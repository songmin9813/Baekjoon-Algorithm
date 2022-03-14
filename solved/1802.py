import sys
def judge(string):
    if len(string)==1:
        return True
    for i in range(len(string)//2):
        if string[i]==string[len(string)-1-i]:
            return False
    return judge(string[:len(string)//2]) and judge(string[len(string)//2+1:])
tc=int(sys.stdin.readline())
for _ in range(tc):
    string=sys.stdin.readline().rstrip()
    print("YES") if judge(string) else print("NO")