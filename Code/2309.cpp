#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int n;
  int sum = 0;
  int first, second;

  vector <int> v;

  for (int i  = 0; i < 9; ++i) {
    int temp;

    cin >> temp;
    sum += temp;
    v.push_back(temp);
  }

  for (int i = 0; i < 9; ++i) {
    for (int j = i + 1; j < 9; ++j) {
      if (sum - v[i] - v[j] == 100) {
       first = i;
       second = j;
      }
    }
  }

  v.erase(v.begin() + first);
  v.erase(v.begin() + second - 1);

  sort(v.begin(), v.end());
  for (int i = 0 ; i < 7; ++i) {
    cout << v[i] << "\n";
  }

  return 0;
}
