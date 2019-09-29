//1260 DFS

#include <cstdio>
#include <iostream>

using namespace std;

int m, n, v;
int a, b;
int arr[1001][1001];
int flag[1001] = {0,};

void dfs(int start){

    printf("%d ", start);
    for ( int i = 1 ; i <= n ; i++ ){
        if(arr[start][i] == 1 && flag[i]==0){
            flag[i] = 1;
            dfs(i);
        }
    }
}


int main(){

    //arr 0으로 초기화
    memset(arr, 0, sizeof(arr));
    
    cin >> n >> m >> v ;

    for (int i =0 ; i < m ; i++){
    
        cin >> a >> b;
        arr[a][b] = 1;

        arr[b][a] = 1;
    
    }

    flag[v] = 1;

    dfs(v);

}