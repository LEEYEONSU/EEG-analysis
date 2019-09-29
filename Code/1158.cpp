#include <cstdio>
#include <queue>
#include <iostream>

using namespace std;

int main(){
  
  int n, k;

  queue<int> q;

  cin >> n >> k ;

  for(int i = 1 ; i <= n ; i++) q.push(i);

  cout << "<" ;
  while(!q.empty()){
    if(q.size()==1){
      cout << q.front() << ">" << endl;
      q.pop();
      break;
    }
    for(int i = 1 ; i < k ; i++){
      q.push(q.front());
      q.pop();
    }
    cout << q.front() << ", ";
    q.pop();
  }  
  return 0;
}
