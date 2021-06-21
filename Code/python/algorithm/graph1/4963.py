from collections import deque

def bfs(i, j, m, n):
    global visited
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            next_x = x + dx
            next_y = y + dy 
            if 0 <= next_x < m and 0 <= next_y < n:
                if board[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = 1

ans = []
while True:
    n, m = map(int, input().split())

    if n == 0 and m ==0 :
        break 
    
    board = [list(map(int, input().split())) for _ in range(m)]
    visited = [[0]*n for _ in range(m)] 

    island = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j, m, n)
                island += 1
    print(island)
    

