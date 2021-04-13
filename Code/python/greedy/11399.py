
n = int(input())

people = list(map(int, input().split()))
people = sorted(people)

ans = 0 
for i in range(n):
    ans += people[i]*(n-i)

print(ans)