# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def solve(x, y, count):
    global ans, sum_MAP, paper_sum

    if y >= 10 :
        ans = min(ans, count)
        return

    if x >= 10 :
        solve(0, y+1, count)
        return

    if board[x][y]:
        for k in range(5):
            if paper[k] == 0:
                continue
            if x + k >= 10 or y + k >= 10:
                continue

            flag = 0
            for i in range(x, x+k+1):
                for j in range(y, y + k +1):
                    if board[i][j] == 0 :
                        flag = 1
                        break
                if flag :
                    break

            if not flag :
                for i in range(x, x+k+1):
                    for j in range(y, y+k+1):
                        board[i][j] = 0

                paper[k] -= 1
                solve(x+k+1, y, count + 1)
                paper[k] += 1

                for i in range(x, x+k+1):
                    for j in range(y, y+k+1):
                        board[i][j] = 1
    else :
        solve(x+1, y, count)

ans = 25
board = [list(map(int, input().split())) for _ in range(10)]
paper = [5, 5, 5, 5, 5]

solve(0, 0, 0)

if ans == 25 :
    print(-1)
else : print(ans)

