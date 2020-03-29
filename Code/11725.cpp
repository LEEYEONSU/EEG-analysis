#include <stdio.h>
#include <iostream>
#include <queue>

using namespace std;

int main(void){

        int N,a,b;
        queue <int> q;

        int parent[100];
        int check[100] ={0,};
        int arr[100000][100000];

        scanf("%d", &N);

        for (int i = 0 ; i < N-1; i ++){
                scanf("%d %d", &a, &b);
                arr[a][b] = 1;
                arr[b][a] = 1;
        }

        check[1] = 1; parent[1]=0;q.push(1);
        while(!q.empty()){
                int x = q.front(); q.pop();
                for( int j = 1;   j < N+1 ; j++ ) {
                        if(arr[x][j] == 1 && check[j] == 0){
                                check[j] = 1;
                                parent[j] = x;
                                q.push(j);
                        }
                }
        }
        for(int i = 2 ; i < N+1; i ++) printf("%d\n", parent[i]);

        return 0 ;
}