

n = int(input())
last, ans = 0, 0 

time = [ list(map(int, input().split())) for _ in range(n) ]

time = sorted(time, key = lambda x : x[0])
time = sorted(time, key = lambda x : x[1]) 

for s, e in time : 
    if s >= last : 
        ans += 1
        last = e

print(ans)