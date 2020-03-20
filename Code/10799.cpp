#include <cstdio>
#include <stack>
#include <string>
#include <iostream>
using namespace std;

int main(){

  stack<char> st;
  string str;
  int result =0;

  cin >> str;

  for(int i = 0; i < str.length() ; i++){
    if(str[i] == '(') st.push(str[i]);
    else{
      st.pop();
      if(str[i-1]=='(')
        result += st.size();
      else result++;       
    }
  }
  cout << result << endl;
  return 0;

}
