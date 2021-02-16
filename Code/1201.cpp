#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){

        int N, M, K;
        int index = 0;
        int tmp;

        cin >> N >> M >> K;
        vector<int> arr(N);

        for (int i = 0 ; i < N ; i ++) arr[i] = i + 1;

        if( N >= M+K-1 && N <= M*K ){   

                for( int i = 1; i <= M ; i++){
                        
                        tmp =  min(K + index, N-M+i );
                        reverse(arr.begin() + index, arr.begin() + tmp );
                        index = tmp ;
                        for (int i = 0 ; i < N ; i ++) printf("%d", arr[i]);
                        printf("\n");
                }
                for (int i = 0 ; i < N ; i ++) printf("%d", arr[i]);
        }

        else  printf("-1\n");

        return 0;
}