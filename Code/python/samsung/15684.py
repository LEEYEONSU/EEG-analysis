
def check():
    for start in range(N):
        i = start
        for j in range(H):
            if board[j][i] == 1 : i+= 1
            elif i > 0 and board[j][i-1] == 1 : i -= 1
        if i != start : return False
    return True

def dfs(cnt, n, r):
    global ans

    if cnt == r : 
        if check():
            ans = cnt 
        return 

    for idx in range(n + 1, len(candidates)):
        i, j = candidates[idx]
        if board[i][j] == 1 : continue
        if j > 0 and board[i][j-1] == 1 : continue 
        if board[i][j-1] == 0 and board[i][j+1] ==0 :
            board[i][j] = 1
            dfs(cnt + 1, idx, r)
            board[i][j] = 0 

if __name__ == '__main__':

    N, M, H = map(int, input().split())
    board =[[0] * (N) for _ in range(H)]

    if M == 0 :
        print(0)
        exit(0)

    for _ in range(M):
        a, b = map(int, input().split())
        board[a-1][b-1] = 1

    candidates = []
    for i in range(H):
        for j in range(N-1):
            if board[i][j] ==0 and board[i][j+1] == 0 and board[i][j-1] ==0 :
                candidates.append([i, j])

    ans, flag = 4, 1
    for r in range(4):
        dfs(0,-1, r)
        if ans < 4 : 
            print(ans)
            flag = 0 
            break

    if flag == 1 : print(-1)

    

    





