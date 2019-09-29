#include <cstdio>
#include <iostream>

using namespace std;

int arr[101] = {0, };

int fibonacci(int n){

    if (arr[n] != 0) return arr[n];
    arr[n] = fibonacci(n - 1) + fibonacci(n - 2);    
    printf("%d\n", arr[n]);

    return arr[n];
}

int main(){
    int n = 100;
    arr[0] = arr[1] =1;
    fibonacci(n);


}