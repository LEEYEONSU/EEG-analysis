import sys 

sys.setrecursionlimit(10000) 

n = int(input()) 
tree = [[] for _ in range(n+1)] 

for _ in range(n-1): 
    a, b = map(int, input().split()) 
    tree[a].append(b) 
    tree[b].append(a) 
    
parents = [0 for _ in range(n+1)] 
parents[1] = 1 

def dfs(curr, tree, parents): 
    for node in tree[curr]: 
        if parents[node] == 0: 
            parents[node] = curr 
            dfs(node, tree, parents) 

dfs(1, tree, parents) 

print(*parents[2:])

