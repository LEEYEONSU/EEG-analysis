#include <stdio.h>
#include <iostream>

using namespace std;
#define mod 10007

int main(void){

        int D[1001][10] = {0,};
        int N;

        scanf("%d", &N);

        for(int  i = 0 ; i <= 9; i++ ) D[1][i] = 1;
        for (int i = 2 ; i <= N ; i ++){
                for(int  j = 0 ; j <=9 ; j ++){
                        for(int  k = j ; k <= 9 ; k++){
                                D[i][k] += D[i-1][j];
                                D[i][k] %= mod;
                        }
                }
        } 

        long long ans = 0;
        for ( int i = 0 ; i <= 9 ; i ++)  ans += D[N][i];
        
        ans %= mod;
        printf("%lld\n", ans);

        return 0;


}