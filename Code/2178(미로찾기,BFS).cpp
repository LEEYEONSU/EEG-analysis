#include <stdio.h>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;
int main(){
    int n,m;
    bool check[101][101] = {false, };
    int ans[101][101] = {0, };
    cin >> n >> m ;
    int miro[103][103];
    int dx[4] = {1,0,-1,0};
    int dy[4] = {0,1,0,-1};

    for (int i =1; i<=n; i++){
        for (int j=1; j<=m; j++)
            scanf("%1d",&miro[i][j]);
    }

    queue <pair <int,int> > q;
    q.push(make_pair(1,1));
    check[1][1] = true;
    ans[1][1] = 1;

    while(!q.empty()){
        pair<int, int> x = q.front();
        q.pop();

        for (int i=0;i<4;i++){
            int xx = x.first + dx[i];
            int yy = x.second + dy[i];
            if(xx >= 1 && xx <= n && yy >= 1 && yy <= m &&  miro[xx][yy] == 1 && check[xx][yy]==false){
                ans[xx][yy] = ans[x.first][x.second] + 1;
                check[xx][yy] = true;
                q.push(make_pair(xx,yy));
            }
        }   
    }
    printf("%d\n", ans[n][m]);
    
}