import sys
sys.setrecursionlimit(10**5)
#전위 탐색이 곧 dfs다. 이진 탐색 트리 시점으로 문제를 다시 봐보자. 단순 구현에 가깝다
dict_={}
num,root=0,0
def postorder(num):
    if num!=0:
        postorder(dict_[num][0])
        postorder(dict_[num][1])
        print(num)
root=int(sys.stdin.readline())
dict_[root]=[0,0]
while True:
    try:
        num=int(sys.stdin.readline())
        dict_[num]=[0,0]
        tmproot=root
        while True:
            if tmproot>num:
                if dict_[tmproot][0]==0:
                    dict_[tmproot][0]=num
                    break
                else:
                    tmproot=dict_[tmproot][0]
            else:
                if dict_[tmproot][1]==0:
                    dict_[tmproot][1]=num
                    break
                else:
                    tmproot=dict_[tmproot][1]
    except:
        break
postorder(root)