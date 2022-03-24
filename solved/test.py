from collections import deque#BFS를 사용하기 위한 import
import copy#각 퍼즐의 상태 복사본을 만들기 위한 import
import heapq#최소값을 빼내기 위한 힙큐 import
puzzles=[['1','2','3'],['4',' ','5'],['7','8','6']]
ans=[['1','2','3'],['4','5','6'],['7','8',' ']]

all_nodes={'A':puzzles}
alphabet='B'
gn=0#깊이 확인을 위한 변수 설정

def make_node(puzzles,open,closed):
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    hn=[1,2,3,4]#휴리스틱 가중치
    #탐색의 순서는  right,down,left,up순임을 알 수 있음
    for i1 in range(3):
        for i2 in range(3):
            if puzzles[i1][i2]==' ':#이 순간부터 노드를 만들어야 함 
                for i3 in range(4):
                    newX=i1+dx[i3]
                    newY=i2+dy[i3]
                    if 0<=newX<3 and 0<=newY<3:#새로운 위치가 범위 안에 들어있는 경우
                        new_puzzles=copy.deepcopy(puzzles)
                        new_puzzles[i1][i2]=new_puzzles[newX][newY]
                        new_puzzles[newX][newY]=' '
                        #복사본 생성 후 swap
                        existed=False
                        for fn,check in open:
                            if new_puzzles==all_nodes[check]:
                                existed=True
                        for check in closed:
                            if new_puzzles==all_nodes[check]:
                                existed=True
                                #open, closed에 이미 노드가 있는지 확인
                        if not existed: # #open에 들어가야 하는 순간
                            global alphabet,gn
                            all_nodes[alphabet]=new_puzzles
                            heapq.heappush(open,[hn[i3]+gn,alphabet])
                            alphabet=chr(ord(alphabet)+1)
                return#노드 생성은 빈칸 기준으로 최대 4번만 하면 됨

def breadth_first_search(start):
    global gn
    open=[]
    closed=deque()
    heapq.heappush(open,[0,start])#초기 f(n)은 0으로 세팅
    while open:
        length=len(open)
        for _ in range(length):#한 사이클이 곧 한 번의 깊이 확인임
            fn,current_alphabet=heapq.heappop(open)
            if all_nodes[current_alphabet]==ans:
                print('목표 노드 발견! 생성된 노드는 '+str(len(all_nodes))+'개 입니다.')
                return True
            closed.appendleft(current_alphabet)
            make_node(all_nodes[current_alphabet],open,closed)
            #노드의 생성이 이루어져야 함
            print('open='+str(list(open))+'; closed='+str(list(closed)))
    gn+=1
    return False

breadth_first_search('A')