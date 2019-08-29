#include<iostream>
#include<algorithm>
using namespace std;

// result: https://atcoder.jp/contests/abc120/submissions/7170539

int main() {
  string S;
  cin >> S;
  int red = 0;
  int blue = 0;
  for (int i = 0; i < S.length(); i++) {
    if (S[i] == '0') red += 1;
    else blue += 1;
  }
  cout << min(red, blue) * 2 << endl;
}
