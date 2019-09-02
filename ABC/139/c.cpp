#include<iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  int ans = 0;
  int h[n];
  for (int i = 0; i < n; i++) {
    cin >> h[i];
  }

  int cur_length = 0;
  for (int i = 0; i < n; i++) {
    if (h[i] <= h[i + 1]) {
      cur_length += 1;
      ans = max(cur_length, ans);
    } else {
      cur_length = 0;
    }
  }

  cout << ans << endl;
}
