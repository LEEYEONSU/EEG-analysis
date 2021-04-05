import copy
from collections import deque

def make_wall( count ) :
    for i in range(N*M):
        if board[i//M][i%M] != 0: continue
        board[i//M][i%M] = 1
        
        for j in range(i+1, N*M):
            if board[j//M][j%M] != 0 : continue
            board[j//M][j%M] = 1

            for k in range(j+1, N*M):
                if board[k//M][k%M] != 0 : continue
                board[k//M][k%M] = 1
                bfs()
                board[k//M][k%M] = 0 
            board[j//M][j%M] = 0 
        board[i//M][i%M] = 0 

def bfs():
    global answer
    board_tmp = copy.deepcopy(board)
    for i in range(N):
        for j in range(M):
            if board_tmp[i][j] == 2 : 
                q.append([i,j])

    while q : 
        x, y = q.popleft()
        for dx, dy in direction :
            nx = x + dx
            ny = y + dy
            if 0<= nx < N and 0<= ny < M and board_tmp[nx][ny] == 0 :
                board_tmp[nx][ny] = 2 
                q.append([nx, ny])

    zero_cnt = 0 
    for i in board_tmp:
        for j in i : 
            if j == 0 : zero_cnt += 1
    answer = max(answer, zero_cnt)

direction = [(0,-1), (0,1), (1,0), (-1,0)]
N, M = map(int,input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]
q = deque()
answer = 0 
make_wall(0)
print(answer)

