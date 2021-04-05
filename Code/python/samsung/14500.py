
N, M = map(int, input().split())
board = [ list(map(int, input().split())) for _ in range(N) ]

tetromino = [
                    [(0,0), (0,1), (0,2), (0,3)],
                    [(0,0), (1,0), (2,0), (3,0)], 

                    [(0,0), (0,1), (1,0), (1,1)],

                    [(0,0), (1,0), (2,0), (2,1)],
                    [(0,0), (0,1), (1,1), (2,1)],
                    [(0,0), (1,0), (1,1), (1,2)],
                    [(1,0), (1,1), (1,2), (0,2)],
                    [(0,0), (0,1), (0,2), (1,0)],
                    [(0,0), (0,1), (0,2), (1,2)],
                    [(0,0), (0,1), (1,0), (2,0)],
                    [(0,1), (1,1), (2,1), (2,0)],

                    [(0,0), (1,0), (1,1), (2,1)],
                    [(0,1), (0,2), (1,0), (1,1)],
                    [(0,1), (1,1), (1,0), (2,0)],
                    [(0,0),(0,1),(1,1),(1,2)],

                    [(0,0),(1,0),(2,0),(1,1)],
                    [(0,1), (1,0), (1,1), (2,1)],
                    [(0,1),(1,0),(1,1),(1,2)],
                    [(0,0), (0,1),(0,2),(1,1)]
]

def sum_of_map(dx, dy, tmp):
    s_um = 0 
    global N, M, board
    for (x, y) in tmp:
            next_x = x + dx
            next_y = y + dy 
            if 0 <= next_x < N and 0 <= next_y < M:
                s_um += board[next_x][next_y]
            else:  return -1  
    return s_um

ans = 0
for i in range(N):
    for j in range(M):
        for tmp in tetromino:
            sum_tmp = sum_of_map(i, j, tmp)
            if ans < sum_tmp :
                ans =  sum_tmp
print(ans)
