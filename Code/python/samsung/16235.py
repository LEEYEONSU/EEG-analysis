from collections import defaultdict


N, M, K = map(int, input().split())
board = [ [5]*N for _ in range(N)]

A = [ list(map(int, input().split())) for _ in range(N) ]

tree_info = defaultdict(lambda : [])
for _ in range(M):
    x, y, z   = map(int, input().split())
    tree_info[(x - 1, y - 1)].append(z)

for _ in range(K):
    dead_tree = []
    #spring
    for key in tree_info.keys():
        live_tree = []
        for i in range(len(tree_info[key])):
            x, y, z = key[0], key[1], tree_info[key][i]
            if board[x][y] >= z : 
                board[x][y]  -= z
                tree_info[key][i] += 1
                live_tree.append(tree_info[key][i])
            else : 
                dead_tree.append([key, z])
        tree_info[key] = live_tree
    
    # summer
    if dead_tree :
        for (x_,y_), z_ in dead_tree :
            board[x_][y_] += z_ // 2
    
    # fall
    direction = [(-1,-1), (-1,0), (-1, 1), (0,-1), (0,1), (1, -1), (1,0), (1, 1)]
    tmp = []
    for key in tree_info.keys():
        tmp.append(key)
    for key in tmp :
        for age in tree_info[key]:
            if age%5 == 0 : 
                x, y = key[0], key[1]
                for dx, dy in direction :
                    if  0 <= x + dx < N and 0 <= y + dy < N : 
                        tree_info[(x + dx, y + dy)] = [1] + tree_info[(x + dx, y + dy)] 

    # winter
    for i in range(N):
        for j in range(N):
            board[i][j] += A[i][j] 

cnt = 0 
for value in tree_info.values():
    cnt += len(value)

print(cnt)






            


                    


