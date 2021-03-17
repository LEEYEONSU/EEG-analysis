



check = [0] * 250000
A, P = map(int, input().split())
count = 1
print(dfs(A, P, count, check))
