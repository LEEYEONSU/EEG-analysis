
N = int(input())
Table = [ list(map(int, input().split())) for _ in range(N) ]

max_pay = [0]*N
for i in range(N-1, -1, -1):
    day = Table[i][0]
    pay = Table[i][1]

    if day > N - i :
        if i != N-1 : 
            max_pay[i] = max_pay[i+1]
        continue

    if i == N - 1  : 
        max_pay[i] = pay
    elif i + day == N : 
        max_pay[i] = max(pay, max_pay[i+1])
    else :
        max_pay[i] = max(max_pay[i + day] + pay, max_pay[i+1])

print(max_pay[0])
