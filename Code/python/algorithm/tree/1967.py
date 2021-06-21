import sys

sys.setrecursionlimit(1000000)
v = int(input())

node_graph = [[] for _ in range(v + 1)]

for _ in range(v-1):
    path = list(map(int, sys.stdin.readline().split()))
    node_graph[path[0]].append([path[1], path[2]])
    node_graph[path[1]].append([path[0], path[2]])

result_first = [ 0 for _ in range(v+1)]

def DFS(start, matrix, result):
    for e, d in matrix[start]:
        if result[e] == 0 :
            result[e] = result[start] + d
            DFS(e, matrix, result)

DFS(1, node_graph, result_first)
result_first[1] = 0 

tmp_max, index = 0, 0 
for i in range(len(result_first)):
    if tmp_max < result_first[i]:
        tmp_max = result_first[i]
        index = i 

result_final = [0 for _ in range(v+1)]

DFS(index, node_graph, result_final)
result_final[index] = 0 
print(max(result_final))


    