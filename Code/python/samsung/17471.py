from itertools import combinations
from collections import deque
import math

def check(group, board):

    visited = set()
    q = deque()
    q.append(group[0])
    count = 1
    visited.add(group[0])

    while q:
        tmp = q.popleft()
        for x in range(1,len(group)):
            if board[tmp][group[x]] == 1 and group[x] not in visited:
                visited.add(group[x])
                q.append(group[x])
                count += 1

    if count == len(group):
        return True
    return False


N = int(input())
loc_info = list(map(int, input().split()))
MAP = [[0] * N for _ in range(N)]

max_val = sum(loc_info)
for i in range(N):
    info = list(map(int, input().split()))
    for j in range(1, info[0]+1):
        MAP[i][info[j]-1] = 1

for i in range(1, (N//2 + 1)):
    candidates = combinations(range(N), i)
    for candi in candidates:
        part_one = list(candi)
        part_two = list(set(range(N)) - set(part_one))
        if check(part_one, MAP) and check(part_two, MAP):
            part_one_sum, part_two_sum = 0, 0
            for k in range(i):
                part_one_sum += loc_info[part_one[k]]
            for k2 in range(N-i):
                part_two_sum += loc_info[part_two[k2]]
            max_val = min(max_val, abs(part_two_sum - part_one_sum))

if max_val == sum(loc_info) :
    print(-1)
else :
    print(max_val)




