//1260 BFS

#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

int main(){

    int m, n, v;
    int a, b;
    int arr[1001][1001];
    int flag[1001] = {0,};
    queue <int> q;

    //arr 0으로 초기화
    memset(arr, 0, sizeof(arr));


    cin >> n >> m >> v ;

    for (int i =0 ; i < m ; i++){
    
        cin >> a >> b;
        arr[a][b] = 1;

        arr[b][a] = 1;
    
    }

    flag[v] = 1;
    q.push(v);

    while ( !q.empty() ){
        
        int start = q.front();

        printf("%d ", start);

        q.pop();
        

        for ( int j = 1; j <= n ; j++){
            
            if( arr[start][j] == 1 && flag[j] != 1){
                flag [j] = 1;
                q.push(j);

            }
            else continue;
            
            
        }

        
    }
    puts("");


}