
def dfs(v):

    visited[v] = 1

    if visited[v] == arr[v]:
        return 

    if visited[arr[v]] == 0:
        dfs(arr[v])

t = int(input())
for _ in range(t):

    n = int(input())
    count = 0
    arr = [0] + list(map(int, input().split()))

    visited = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i)
            count += 1

    print(count)



