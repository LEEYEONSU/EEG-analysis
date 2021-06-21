import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = 1
    for i in MAP[v]:
         if visited[i] == 0:
            dfs(i)

N, M = map(int, input().split())
MAP = [[] for _ in range(N)]
visited = [0]*N

for i in range(M):
        a, b = map(int, input().split())
        MAP[a-1].append(b-1)
        MAP[b-1].append(a-1)

count = 0 
for i in range(N):
    if visited[i] == 0:
        dfs(i)
        count += 1

print(count)
