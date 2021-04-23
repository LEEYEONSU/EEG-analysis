from itertools import combinations
from copy import deepcopy
from heapq import heappop, heappush


def attack(archer_pos):
    global MAP

    attacked = [[False for _ in range(m)] for _ in range(n)]
    remove_list = []
    cnt = 0 

    for pos in archer_pos : 
        pq = []
        # from nearest 
        for i in range(n-1, -1, -1):
            for j in range(m):
                if MAP[i][j] == 1 : 
                    distance = abs(n-i) + abs(pos - j)
                    if distance <= d : 
                        heappush(pq, [distance, j, i])
        
    # print(enemy_pos)
            if pq: 
                dist, x, y = heappop(pq)
                remove_list.append([y,x])
    
    # print('remove' , remove_list)
    for y, x in remove_list : 
        if not attacked[y][x] :
            attacked[y][x] = True
            cnt += 1
            MAP[y][x] = 0 

    return cnt

def move_enemy():
    global MAP 
    MAP[-1] = [0 for _ in range(m)]
    for i in range(-1, -n, -1 ):
        MAP[i] = MAP[i-1]
    MAP[0] = [0 for _ in range(m)]

def get_enemy_count():
    global MAP
    cnt = 0 
    for i in range(n):
        for j in range(m):
            if MAP[i][j] == 1 : cnt += 1 
    return cnt

def game(archer):
    cnt = 0 
    
    while get_enemy_count() != 0 :
        cnt += attack(archer)
        move_enemy()
    return cnt

##############################################
n, m, d = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(n) ]
answer = 0 

castle_pos = [i for i in range(m)]
archer = tuple(combinations(castle_pos, 3))

for i in range(len(archer)):
    MAP = [[board[i][j] for j in range(m)] for i in range(n)]
    cnt = game(archer[i])
    if answer < cnt : answer = cnt 

print(answer)

