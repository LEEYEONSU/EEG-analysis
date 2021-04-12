import sys

v = int(sys.stdin.readline())

node_graph = [[] for _ in range(v+1)]

for i in range(v):
    path = list(map(int, sys.stdin.readline().split()))

    len_p = len(path)
    for i in range(1,  len_p//2):
        node_graph[path[0]].append([path[2*i - 1], path[2*i]])

result_first = [ 0 for _ in range(v+1)]

def DFS(start, matrix, result):

    for e, d in matrix[start] :
        if result[e] == 0 :
            result[e] = result[start] + d
            DFS(e, matrix, result)

DFS(1, node_graph, result_first)
result_first[1] = 0 

tmpmax = 0 
index = 0 

for i in range(len(result_first)):
    if tmpmax < result_first[i]:
        tmpmax = result_first[i]
        index = i 

result_final = [0 for _ in range(v+1)]
DFS(index, node_graph, result_final)
result_final[index] = 0 
print(max(result_final))