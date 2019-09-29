#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<string>

using namespace std;

int main(void){

    int A,B,C,D=0;

    long long a, b;

    cin >> A >> B >> C >> D;

    string s1 = to_string(A) + to_string(B);
    string s2 = to_string(C) + to_string(D);

    a = stoll(s1); //string 을 longlong
    b = stoll(s2);
    cout << a+b << endl;

    return 0;
}
        
