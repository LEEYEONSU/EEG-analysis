import sys 

### TEST CASE input
input = sys.stdin.readline
s = []
K, N = map(int, input().split())
for i in range(K): 
    s.append(int(input()))

start, end = 1, max(s)

### algorithm 
while start <= end :

    mid = (start + end) // 2
    tmp = 0 
    for i in s:
        tmp += i  // mid

    if tmp >= N :
        start = mid + 1
    else : 
        end = mid  - 1

print(end)
