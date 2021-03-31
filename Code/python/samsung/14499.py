if __name__ == '__main__':

    H, W, x, y, n = list(map(int, input().split()))
    Board = [ list(map(int, input().split())) for _ in range(H)]
    cmd = list(map(int, input().split()))
    dice = [0,0,0,0,0,0]

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    for i in range(n):
        if  y + dy[cmd[i]-1]  < 0 or y + dy[cmd[i]-1] >= W or x + dx[cmd[i]-1] < 0 or x + dx[cmd[i]-1] >= H :
            continue
        else : 
            x += dx[cmd[i] - 1]
            y += dy[cmd[i] - 1]

            if cmd[i] == 1 : 
                dice[0], dice[2], dice[5], dice[3] = dice[2], dice[5], dice[3], dice[0]

            elif cmd[i] == 2 :
                dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]

            elif cmd[i] ==  3 :
                dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

            elif cmd[i] == 4 :
                dice[0], dice[4], dice[5], dice[1] = dice[4], dice[5], dice[1], dice[0] 

            if Board[x][y] == 0 : Board[x][y] = dice[5]
            else : 
                dice[5] = Board[x][y]
                Board[x][y] = 0 

            print(dice[0])
