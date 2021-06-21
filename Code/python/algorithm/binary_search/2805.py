import sys

input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))
start, end = 1, max(a)

while start <= end:
    mid = (start + end) // 2

    tree = 0 
    for i in range(N):
        if mid < a[i]:
            tree += a[i] - mid

    if tree >= M : 
        start = mid + 1
    else :
        end = mid - 1

print(end)
