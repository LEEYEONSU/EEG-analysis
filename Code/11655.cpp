#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int main(){

        string str;
        int str_len;
        char temp[1001];

        getline(cin, str);
        str_len = str.length();

        for ( int i = 0 ; i < str_len; i ++){
                if (str[i] >= 'A' && str[i] < 'A' + 13 || str[i]>='a' && str[i]<'a'+13){
                        temp[i] = str[i] + 13;
                }
                else if ( str[i] >= '0' && str[i] <= '9' || str[i] == ' '){
                        temp[i] = str[i];
                }
                else{
                        temp[i] = str[i]-13;       
                }

                cout << temp[i];
        }

        cout << "\n";
        
        return 0;

}