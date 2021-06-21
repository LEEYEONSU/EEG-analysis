from collections import deque

def bfs(v, color):

    color[v] = 1
    q = deque()
    q.append(v)

    while q:
        now = q.popleft()
        for next in adj_arr[now]:
            if  color[next] == 0:
                color[next] =  -color[now]
                q.append(next)

            else :
                if color[next] == color[now]:
                    return False
    return True 
    
a = int(input())
for _ in range(a):
    flag = True
    n, m = map(int, input().split())
    adj_arr = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        adj_arr[a-1].append(b-1)
        adj_arr[b-1].append(a-1)
    
    color = [0 for _ in range(n)]

    for node in range(n):
        if color[node] == 0 :
            if not bfs(node, color):
                flag = False
                break
    
    if not flag:
        print('NO')
    else :
        print('YES')