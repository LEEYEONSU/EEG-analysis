from collections import deque

def go_turn( direction ):

    if direction == 0 :
        new_direction = 3
        dx, dy = (-1,0)
    elif direction == 1 :
        new_direction = 0
        dx, dy = (0,-1)
    elif direction == 2 :
        new_direction = 1
        dx, dy = (1,0)
    else :
        new_direction = 2
        dx, dy = (0, 1)

    return new_direction, dx, dy 

def go_back( direction ):

    if direction == 0 : dx, dy = (0,1)
    elif direction == 1 : dx, dy = (-1,0)
    elif direction == 2 : dx, dy = (0,-1)
    else : dx, dy = (1, 0)

    return dx, dy 

if __name__ == '__main__' :

    N, M = map(int, input().split())
    x, y, direction = map(int, input().split())

    board = [ list(map(int, input().split())) for _ in range(N)]
    visited = [ [0]*M for _ in range(N)]

    visited[x][y] = 1
    cnt = 1

    while True : 

        n_direction, dx, dy = go_turn(direction)
        nx = x + dx
        ny = y + dy

        if board[nx][ny] == 0 and 0 <= nx < N and 0 <= ny < M : 
            if visited[nx][ny] == 0 : 
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1

            else : continue
            direction = n_direction

        else :
            bx, by = go_back(direction)
            nx , ny = x + bx, y + by

            if 0 <= nx < N and 0 <= ny < M :
                if board[nx][ny] != 0  :
                    break
                else :
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = 1 
                        cnt += 1 
                    q.append((nx, ny))

    print(cnt)

            
                

