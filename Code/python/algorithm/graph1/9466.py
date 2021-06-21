import sys
sys.setrecursionlimit(111111)

def dfs(v):
    global result
    visited[v] = 1
    cycle.append(v)

    if visited[students[v]] == 1:
        if students[v] in cycle:
            result += cycle[cycle.index(students[v]):]
        return
    else :
        dfs(students[v])

t = int(input())
for _ in range(t):
    n = int(input())
    visited = [0] + [0 for _ in range(1, n+1)]
    students = [0] + list(map(int, input().split()))
    result = []

    for v in range(1, n+1):
        if visited[students[v]] == 0:
            cycle = []
            dfs(v)

    print(n - len(result))