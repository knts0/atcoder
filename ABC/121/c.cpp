#include<iostream>
#include<algorithm>
using namespace std;

// result: https://atcoder.jp/contests/abc121/submissions/4523696

int main() {
  int N, Q;
  cin >> N >> Q;
  string S;
  cin >> S;
  int l[Q], r[Q];
  for (int i = 0; i < Q; i++) {
    cin >> l[i] >> r[i];
  }

  int count_ac[N];
  count_ac[0] = 0;
  for (int i = 0; i < N - 1; i++) {
    if (S[i] == 'A' && S[i + 1] == 'C') count_ac[i + 1] = count_ac[i] + 1;
    else count_ac[i + 1] = count_ac[i];
  }

  for (int i = 0; i < Q; i++) {
    cout << count_ac[r[i] - 1] - count_ac[l[i] - 1] << endl;
  }
}
