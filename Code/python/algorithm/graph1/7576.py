from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        now_x, now_y = q.popleft()
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            next_x = now_x + dx
            next_y = now_y + dy
            if 0<=next_x<m and 0<=next_y<n and MAP[next_x][next_y] == 0:
                q.append((next_x, next_y))
                MAP[next_x][next_y] = MAP[now_x][now_y] + 1
            

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    for j in range(n):
        if MAP[i][j] == 1:
            bfs(i,j)

is_True = False 
for i in range(m):
    for j in range(n):
        if MAP[i][j] == 0: 
            is_True = True
            break

if is_True:
    print(-1)

elif max(max(MAP)) == -1:
    print(0)
else :
    print(max(max(MAP))-1)
