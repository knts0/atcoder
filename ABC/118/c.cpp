#include<iostream>
using namespace std;

// https://atcoder.jp/contests/abc118/submissions/7185601

int gcd(int a, int b) {
  if (b == 0) return a;
  else return gcd(b, a % b);
}

int main() {
  int N;
  cin >> N;
  int A[100010];

  for (int i = 0; i < N; i++) {
    cin >> A[i];
  }

  int ans = A[0];
  for (int i = 0; i < N; i++) {
    ans = gcd(A[i], ans);
  }

  cout << ans << endl;
}
