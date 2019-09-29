#include <cstdio>
#include <queue>
#include <iostream>

using namespace std;

int main(){
  
  int output_num[27] = {0};
  char ch[101];

  scanf("%s", ch);

  for(int i = 0; i<strlen(ch)+1; i++){
    int p;   
    p = int(ch[i])-'a';
    //printf("%d", p);
    output_num[p]++;
  }
  for (int i = 0 ; i <= ('z'-'a'); i++){
    printf("%d ", output_num[i]);
  }
  printf("\n");
  return 0;
}
