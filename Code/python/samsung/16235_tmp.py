from collections import deque
import copy
import sys

if __name__ == '__main__' : 

    cnt = 0 
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    board = [ [5]*N for _ in range(N)]
    A = [ list(map(int, input().split())) for _ in range(N) ]
    tree_info = {}

    for i in range(N):
        for j in range(N):
            tree_info[(i, j)] = deque()

    for _ in range(M):
        x, y, z   = map(int, input().split())
        tree_info[(x - 1, y - 1)].append(z)
        cnt += 1

    for _ in range(K):
        #spring + summer
        for key in tree_info.keys():
            for i, val in enumerate(tree_info[key]) :
                x, y, z = key[0], key[1], val
                if board[x][y] >= z : 
                    board[x][y]  -= z
                    tree_info[key][i] += 1
                else : 
                    for _ in range(i, len(tree_info[key])):
                        board[x][y] += tree_info[key].pop() // 2
                        cnt -= 1
                    break

        # fall
        direction = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1, -1), (1,0), (1, 1)]
        tmp_tree = copy.deepcopy(tree_info)
        for key in tmp_tree.keys() :
            for age in tmp_tree[key]:
                if age%5 == 0 : 
                    x, y = key[0], key[1]
                    for dx, dy in direction :
                        if  0 <= x + dx < N and 0 <= y + dy < N : 
                            tree_info[(x + dx, y + dy)].appendleft(1)
                            cnt += 1

        # winter
        for i in range(N):
            for j in range(N):
                board[i][j] += A[i][j] 

    print(cnt)
    





                


                       


