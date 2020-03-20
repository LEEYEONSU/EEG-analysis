// 7569번도 풀어보기 

#include <stdio.h>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main(){

    int n, m;
    int tomato[1001][1001];
    bool check[1001][1001] = {false, };
    int num = 1;
    queue <pair <int,int> > q;

    int dx[4] = {1,0,-1,0};
    int dy[4] = {0,1,0,-1};

    scanf("%d %d", &n, &m);

    for (int i = 1 ; i <= m ; i++){
        for (int j = 1 ; j <= n ; j++){
            scanf("%d",&tomato[i][j]); 
            if(tomato[i][j] == num){
                q.push(make_pair(i,j));
                check[i][j] = true;    
            }
        }
    }

    while(!q.empty()){
        pair <int,int> x ;
        x = q.front();
        q.pop();

        for( int i = 0 ; i < 4 ; i++){
            int x_ = x.first + dx[i];
            int y_ = x.second + dy[i];
            if(x_ >= 1 && y_ >= 1 && x_<= m && y_<= n &&tomato[x_][y_] ==0  && check[x_][y_] == false){
                check[x_][y_] = true;
                q.push(make_pair(x_,y_));
                tomato[x_][y_] = tomato[x.first][x.second] + 1 ;
                num = tomato[x_][y_];
            }
        }
    }

    for (int i = 1 ; i <= m; i++){
        for (int j = 1 ; j <= n ; j++){
            if(tomato[i][j] == 0){
                printf("-1\n");
                exit (0);
            }
        }
    }
    printf("%d\n", num-1);

    return 0;
}