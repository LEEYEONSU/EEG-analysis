import sys
from collections import deque

def change_dir(direction, next_dir):
    if next_dir == 'D' : 
        if direction == [1, 0]: return [0, -1]
        elif direction == [-1, 0]: return [0, 1]
        elif direction == [0, 1]: return [1, 0]
        elif direction == [0, -1]: return [-1, 0]
    else:
        if direction == [1, 0]: return [0, 1]
        elif direction == [-1, 0]: return [0, -1]
        elif direction == [0, 1]: return [-1, 0]
        elif direction == [0, -1]: return [1, 0]

if __name__ == '__main__' :
     
    N = int(input())
    K = int(input())
    Board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(K):
        a, b = list(map(int, input().split()))
        Board[a-1][b-1] = 1

    S = int(input())
    
    S_move = deque()
    for i in range(S):
        a, b = list(input().split())
        S_move.append([int(a), b])

    q = deque()
    direction = [0,1]
    q.append([0,0])
    count = 0 

    while q:
        x, y = q[-1][0], q[-1][1]
        x += direction[0]
        y += direction[1]

        if 0 <= x < N and 0 <= y < N :
            if [x, y] in q : 
                break
            q.append([x, y])
            if Board[x][y] == 1:
                Board[x][y] = 0
            else: q.popleft()
        else: break

        count += 1 
        if S_move and count == S_move[0][0] :
            direction = change_dir(direction, S_move[0][1])
            S_move.popleft()

    print(count + 1)






    
        