import sys, copy 

ans = 0 
def dfs(dfs_board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                if ans < dfs_board[i][j] : ans = dfs_board[i][j] 
        return
    
    for opt in ('L', 'R', 'Up', 'Down'):
        dfs(move(copy.deepcopy(dfs_board), opt), cnt + 1)

def move(B, option):

    if option == 'L':
        for i in range(n):
            tmp_sum = 0
            s = 0
            for j in range(n):
                if B[i][j] == 0 : continue
                if tmp_sum == 0 : tmp_sum = B[i][j]
                else:
                    if tmp_sum == B[i][j]:
                        B[i][s] = tmp_sum * 2
                        s = s + 1
                        tmp_sum = 0 
                    else:
                        B[i][s] = tmp_sum
                        s = s + 1
                        tmp_sum = B[i][j]
                B[i][j] = 0 
            if tmp_sum != 0 : B[i][s] = tmp_sum
    
    elif option == 'R':
        for i in range(n):
            tmp_sum = 0 
            s = n - 1
            for j in range(n-1, -1, -1):
                if B[i][j] == 0 : continue
                if tmp_sum == 0 : tmp_sum = B[i][j]
                else:
                    if tmp_sum == B[i][j] :
                        B[i][s] = tmp_sum * 2
                        s = s - 1
                        tmp_sum = 0 
                    else:
                        B[i][s] = tmp_sum
                        s = s - 1
                        tmp_sum = B[i][j]
                B[i][j] = 0 
            if tmp_sum != 0 : B[i][s] = tmp_sum

    elif option == 'Up':
        for i in range(n):
            tmp_sum = 0 
            s = 0
            for j in range(n):
                if B[j][i] == 0 : continue
                if tmp_sum == 0 : tmp_sum = B[j][i]
                else:
                    if tmp_sum == B[j][i]:
                        B[s][i] = tmp_sum * 2
                        s = s + 1
                        tmp_sum = 0 
                    else:
                        B[s][i] = tmp_sum
                        s = s + 1
                        tmp_sum = B[j][i]
                B[j][i] = 0 
            if tmp_sum != 0: B[s][i] = tmp_sum

    elif option == 'Down':
        for i in range(n):
            tmp_sum = 0
            s = n - 1
            for j in range(n-1, -1, -1):
                if B[j][i] == 0 : continue
                if tmp_sum == 0 : tmp_sum = B[j][i]
                else :
                    if tmp_sum == B[j][i]:
                        B[s][i] = tmp_sum * 2
                        s = s - 1
                        tmp_sum = 0 
                    else:
                        B[s][i] = tmp_sum
                        s = s - 1
                        tmp_sum = B[j][i]
                B[j][i] = 0 
            if tmp_sum != 0 : B[s][i] = tmp_sum
    return B

if __name__ == '__main__' :
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0 
    dfs(board, 0)
    print(ans)