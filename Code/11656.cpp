#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){

        string str; 
        string temp[1001];
        int str_len ; 

        cin >> str;
        str_len = str.length();

        for ( int i = 0 ; i < str_len ; i++ ) {
                temp [i] = str.substr(i,str_len);
                // cout << temp[i] << "\n";
        }
        
        sort(temp,temp+str_len);
        for( int i = 0 ; i < str_len ; i ++){
                cout << temp[i] << "\n";
        }

}