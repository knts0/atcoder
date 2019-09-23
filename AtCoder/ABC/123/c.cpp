#include<iostream>
#include<algorithm>
using namespace std;

// result: https://atcoder.jp/contests/abc123/submissions/7199451

int main() {
  long long n, a, b, c, d, e;
  cin >> n >> a >> b >> c >> d >> e;
  long long min_trans = min(a, min(b, min(c, min(d, e))));
  if (min_trans < n) cout << (n - 1) / min_trans + 5  << endl;
  else cout << 5 << endl;
}
