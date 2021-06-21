from collections import deque 

def bfs(x, y):
    tmp_count = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        now_x, now_y = q.popleft()
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            next_x = now_x + dx
            next_y = now_y + dy 
            if 0<=next_x<n and 0<=next_y<n:
                if MAP[next_x][next_y] == 1 and visited[next_x][next_y] == 0:
                    q.append((next_x, next_y))
                    visited[next_x][next_y] = 1
                    tmp_count += 1
    return tmp_count 

n = int(input())
count = 0 
info = []

MAP = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 1 and visited[i][j] == 0 :            
            tmp = bfs(i, j)
            info.append(tmp)
            count += 1

print(count)
info = sorted(info)
for i in range(count):
    print(info[i])
