from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
visited = [[[[0]*m for _ in range(n)]for _ in range(m)]for _ in range(n)]

q = deque()

def init():

    rx, ry, bx, by, depth = 0, 0, 0, 0, 1
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j 
            elif board[i][j] == 'B':
                bx, by = i, j

    q.append((rx, ry, bx, by, depth)) 
    visited[rx][ry][bx][by] = 1

def movemove(x, y, dx, dy):

    count = 0 
    while board[x + dx][y + dy] != '#'  :
        if board[x][y] == 'O' :
            break
        x += dx
        y += dy
        count += 1
    return x, y, count 

def bfs():

    init()

    while q:
        #FIFO
        rx, ry, bx, by, depth = q.popleft()

        if depth > 10 : 
            break

        for dx, dy in ((-1,0), (0,1), (1,0), (0,-1)):
            n_rx, n_ry, r_cnt = movemove(rx, ry, dx, dy)
            n_bx, n_by, b_cnt = movemove(bx, by, dx, dy)

            if board[n_bx][n_by] == 'O':
                continue
            
            if board[n_rx][n_ry] == 'O':
                print(depth)
                return 

            if n_rx == n_bx and n_ry == n_by :
                if r_cnt > b_cnt :
                    n_rx -= dx
                    n_ry -= dy
                else:
                    n_bx -= dx
                    n_by -= dy

            if visited[n_rx][n_ry][n_bx][n_by] != 1 :
                visited[n_rx][n_ry][n_bx][n_by] = 1
                q.append((n_rx, n_ry, n_bx, n_by, depth + 1))      
            
    print(-1)

bfs()