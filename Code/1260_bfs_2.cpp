//1260 BFS

#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(){

    //vector는 동적 배열 
    int n, m, v;
    int a, b;
    vector <int> bfs[1001];
    queue <int> q;
    bool flag[1001] = {false, };

    cin >> n >> m >> v ;

    for (int i = 0; i < m; i++){
        
        cin >> a >> b;

        bfs[a].push_back(b);
        bfs[b].push_back(a);
    }

    flag[v] = true;
    q.push(v);

    while(!q.empty()){

        int start = q.front();
        
        printf("%d ", start);
        q.pop();

        for (int i = 0 ; i < bfs[start].size(); i++){

            if (flag[bfs[start][i]] == false){
                q.push(bfs[start][i]);
                flag[bfs[start][i]]=true;
            }
        }
    }
    puts("");
}