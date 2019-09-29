#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int main(){

    long long int n;
    scanf("%d", &n);

    vector< pair<int,int> > num(n);

    for (int i = 0 ; i < n; i++){
        cin >> num[i].first >> num[i].second;
    }
    sort(num.begin(), num.end());
    for (int i = 0; i < n ; i++){
        printf("%d %d\n",num[i].first, num[i].second);
    }

    return 0;
}