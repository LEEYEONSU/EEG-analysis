//1260 DFS

#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int m, n, v;
int a, b;
int arr[1001][1001];
int flag[1001] = {0,};

void dfs(int v, vector<int> dfs_g[], bool flag[]){

    flag[v] = true;
    printf("%d ", v);

    for (int i = 0 ; i < dfs_g[v].size(); i++){
        int next = dfs_g[v][i];
        if(flag[next] == false){
            dfs(next, dfs_g, flag);
        }
    }

}

int main(){

    int n, m, v;
    int a, b;
    vector <int> dfs_g[1001];
    bool flag[1001] = {false, };

    cin >> n >> m >> v ;

    for (int i = 0; i < m; i++){
        
        cin >> a >> b;

        dfs_g[a].push_back(b);
        dfs_g[b].push_back(a);
    }
    dfs(v, dfs_g, flag);
}