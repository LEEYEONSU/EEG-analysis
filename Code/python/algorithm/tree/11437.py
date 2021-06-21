import sys

sys.setrecursionlimit(10*6)

n = int(input())
node_graph = [[] for _ in range(n+1)]
visited = [i for i in range(1,n+1)]
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    v1, v2 = map(int, input().split())
    node_graph[v1].append(v2)
    node_graph[v2].append(v1)

# make tree
def dfs(root, depth):
    global node_graph, visited, tree
    for node in node_graph[root]:
        if node in visited :
            visited.remove(node)
            tree[node] = (root, depth)
            dfs(node, depth + 1)
            if not visited:
                return

visited.remove(1)
dfs(1,1)

m = int(input())

ans = []
for i in range(m):
    s1, s2 = map(int, input().split())

    while tree[s1][1] != tree[s2][1]:
        if tree[s1][1] > tree[s2][1]:
            s1 = tree[s1][0]
        else: 
            s2 = tree[s2][0]

    while s1 != s2 :
        s1 = tree[s1][0]
        s2 = tree[s2][0]

    ans.append(s1)

for i in range(len(ans)):
    print(ans[i])