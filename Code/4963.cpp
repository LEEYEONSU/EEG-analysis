#include <stdio.h>
#include <iostream>
#include <queue>

using namespace std;

int dx[8] = { 1 ,0 ,-1 ,0 ,-1 ,1 ,1 ,-1 };
int dy[8] = { 0 ,1 ,0 ,-1 ,-1 ,1 ,-1 ,1 };

int n =0 , m  = 0 ;
int island[51][51];
bool flag[51][51] = {false,};

void dfs( int a, int b, int m, int n){

        flag[m][n] = true;

        for(int k = 0; k < 8; k++){
                int x = a + dx[k] ;
                int y = b + dy[k] ;

                if ( x >=0 && y >= 0 && x < m && y < n && island[x][y] == 1 && flag[x][y] == false){
                        flag[x][y] = true;
                        dfs(x,y,m,n);
                }
        }
}

int main(void){

        while (1){
                int result = 0;
                scanf("%d %d", &n, &m);

                if ( m == 0 && n == 0 )
                        break;

                for(int i  = 0 ; i  < m ; i++ ){
                        for(int j = 0 ; j < n; j ++){
                                scanf("%d", &island[i][j]);
                                flag[i][j] = false;
                        }
                }

                for(int i  = 0 ; i  < m ; i++ ){
                        for(int j = 0 ; j < n; j ++){
                                if ( island[i][j] == 1 && flag[i][j] == false){
                                        // printf(" %d %d\n", i, j);
                                        dfs(i, j,m ,n);
                                        result = result +1;
                                }
                        }
                }

                printf("%d\n", result);
        }

        return 0;
}