from copy import deepcopy
from itertools import permutations

def rotation(arr, r, c, s):

    tmp_arr = deepcopy(arr)
    for k in range(s):
        for i in range(c-s+k+1, c+s-k+1):
            tmp_arr[r-s+k][i] = arr[r-s+k][i-1]
        for i in range(r-s+k+1, r+s-k+1):
            tmp_arr[i][c+s-k] = arr[i-1][c+s-k]
        for i in range(c+s-k-1, c-s+k-1, -1):
            tmp_arr[r+s-k][i] = arr[r+s-k][i+1]
        for i in range(r+s-k-1, r-s+k-1, -1):
            tmp_arr[i][c-s+k] = arr[i+1][c-s+k]

    return tmp_arr

N, M, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
rotation_info = [list(map(int, input().split())) for _ in range(K)]

result = []
for tmp in permutations((range(K)),K):
    board = deepcopy(MAP)
    for a in tmp:
        board = rotation(board, rotation_info[a][0]-1, rotation_info[a][1] -1, rotation_info[a][2])
    ans = sum(board[0])
    for i in range(1, N):
        ans = min(ans, sum(board[i]))
    result.append(ans)
print(min(result))

