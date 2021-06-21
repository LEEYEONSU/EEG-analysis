from collections import deque

n, m = map(int, input().split())
MAP = [list(map(int, input())) for _ in range(n)]

q = deque()
q.append((0,0))
MAP[0][0] = 1
while q:
    now_x, now_y = q.popleft()
    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
        next_x = now_x + dx
        next_y = now_y + dy
        if 0<=next_x<n and 0<=next_y<m:
            if MAP[next_x][next_y] == 1:
                q.append((next_x, next_y)) 
                MAP[next_x][next_y] = MAP[now_x][now_y] + 1
    
print(MAP[n-1][m-1])

