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

    for (int i = 0 ; i < m ; ++i){
        for (int j = 0 ; j < n ; ++j){
            scanf("%d",&tomato[i][j]); 
            if(tomato[i][j] == num){
                q.push(make_pair(n,m));
                check[i][j] = true;    
            }
        }
    }

	//

    while(!q.empty()){
        pair <int,int> x ;

        x = q.front();
        q.pop();

        for( int i = 0 ; i < 4 ; i++){
            int x_ = x.first + dx[i];
            int y_ = x.second + dy[i];
            if(tomato[x.first][x.second] >= 1 && check[x.first][x.second] == false){
                check[x.first][x.second] = true;
                q.push(make_pair(x.first,x.second));
                tomato[x.first][x.second] = num + 1;
            }
        }
    }

    for(int i = 0 ; i < n ; i++){
        for(int j = 0 ; j < m ; j++){
            if(tomato[i][j] == 0){
                printf("-1");
            }
            else
            {
                printf("%d", num);
            }
        }
    }
}