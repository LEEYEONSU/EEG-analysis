
n, val = map(int, input().split())
money = [ int(input()) for _ in range(n) ]

cnt = 0 
while val != 0 :
    for i in range(n-1, -1, -1):
        if money[i] > val :
            continue
        else : 
            tmp = val // money[i] 
            cnt += tmp
            val -= money[i] * tmp 
        
print(cnt)
