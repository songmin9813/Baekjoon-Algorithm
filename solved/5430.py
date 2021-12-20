from collections import deque
tc=int(input())
for _ in range(tc):
    command=input()
    n=int(input())
    try:
        list_=list(map(str,input()[1:-1].split(',')))
        if list_[0]=='':
            list_=[]
        else:
            list_=list(map(int,list_))
        d=deque(list_)
        right=True
        index=0
        for value in command:
            if value=='R':
                if right is True:
                    right=False
                else:
                    right=True
            else:
                if right is True:
                    d.popleft()
                else:
                    d.pop()
        string=''
        while d:
            if right is True:
                string+=str(d.popleft())+','
            else:
                string+=str(d.pop())+','
        print('['+string[:-1]+']')
    except:
        print('error')