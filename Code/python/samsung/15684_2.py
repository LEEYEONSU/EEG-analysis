def check():
    for start in range(N):
        i = start
        for j in range(H):
            if board[j][i] == 1 : i+= 1
            elif i > 0 and board[j][i-1] == 1 : i -= 1
        if i != start : return False
    return True

def dfs(cnt, x, y, r):
    global ans

    if cnt == r : 
        if check():
            ans = cnt 
        return 

    for i in range(x, H):
        if i == x : k = y
        else : k = 0 
        for j in range(k, N-1):
            if board[i][j] == 1 : continue
            if j > 0 and board[i][j-1] == 1 : continue
            if board[i][j] == 0 and board[i][j+1] == 0 :
                board[i][j] =1 
                dfs(cnt+1, i, j + 2, r)
                board[i][j] = 0 

if __name__ == '__main__':

    N, M, H = map(int, input().split())
    board =[[0] * (N) for _ in range(H)]
å
    if M == 0 :
        print(0)
        exit(0)

    for _ in range(M):
        a, b = map(int, input().split())
        board[a-1][b-1] = 1

    ans, flag = 4, 1
    for re in range(4):
        dfs(0,0,0, re)
        if ans != 4 : 
            print(ans)
            flag = 0 
            break
    
    if flag == 1 : print(-1)
