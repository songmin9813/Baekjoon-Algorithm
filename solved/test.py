from collections import deque#BFS를 사용하기 위한 import
import copy#각 퍼즐의 상태 복사본을 만들기 위한 import
puzzles=[['1','2','3'],['4',' ','5'],['7','8','6']]
ans=[['1','2','3'],['4','5','6'],['7','8',' ']]
all_nodes={'A':puzzles,'goal':ans}
alphabet='B'

def make_node(al,puzzles,open,closed):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    #탐색의 순서는 right,down,up,left 순임을 알 수 있음
    #다르게 할 경우 순서가 터져버리는 문제 발생
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
                        for check in open:
                            if new_puzzles==all_nodes[check]:
                                existed=True
                        for check in closed:
                            if new_puzzles==all_nodes[check]:
                                existed=True
                                #open, closed에 이미 노드가 있는지 확인
                        if not existed: # #open에 들어가야 하는 순간
                            global alphabet
                            all_nodes[alphabet]=new_puzzles
                            open.append(alphabet)
                            alphabet=chr(ord(alphabet)+1)
                return#노드 생성은 빈칸 기준으로 최대 4번만 하면 됨

def breadth_first_search(start):
    open=deque()
    closed=deque()
    open.append(start)
    while open:
        current_alphabet=open.popleft()
        if all_nodes[current_alphabet]==all_nodes['goal']:
            print('목표 노드 발견! 생성된 노드는 '+str(len(all_nodes)-1)+'개 입니다.')
            return True
        closed.appendleft(current_alphabet)
        make_node(current_alphabet,all_nodes[current_alphabet],open,closed)
        #노드의 생성이 이루어져야 함
        print('open='+str(list(open))+'; closed='+str(list(closed)))
    return False

breadth_first_search('A')