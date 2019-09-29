#include <cstdio>
#include <stack>
#include <string>
#include <iostream>
using namespace std;


int main(){

  int arr[15][15];
  int n, floor, ho;

  cin >> n;

  for (int i = 0 ; i < 15 ; i++) 
    if(i==0){ 
      for( int k = 1; k < 15 ;k++) arr[0][k]=k;
    }
    else{
      for(int j = 1; j < 15; j++) 
        if(j==1) arr[i][j]=1;
        else arr[i][j] = arr[i][j-1] + arr[i-1][j];
    }

  for ( int i = 0 ; i < n ; i++){
    cin >> floor >> ho;
    printf("%d\n", arr[floor][ho]);
  }
  return 0;
}
