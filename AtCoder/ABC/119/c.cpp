#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

// result: https://atcoder.jp/contests/abc119/submissions/7198728

int main() {
  int N, A, B, C;
  cin >> N >> A >> B >> C;
  int l[8];
  for (int i = 0; i < N; i++) {
    cin >> l[i];
  }

  int ans = 1000000000;
  for (int bit = 0; bit < (1 << 2 * N); bit++) {
    int lengthA = 0;
    int cntA = 0;
    int lengthB = 0;
    int cntB = 0;
    int lengthC = 0;
    int cntC = 0;
    for (int i = 0; i < N; i++) {
      int flag = 2 * ((bit >> (2 * i + 1)) & 1) + ((bit >> 2 * i) & 1);
      if (flag == 1) {
        lengthA += l[i];
        cntA += 1;
      }
      if (flag == 2) {
        lengthB += l[i];
        cntB += 1;
      }
      if (flag == 3) {
        lengthC += l[i];
        cntC += 1;
      }
    }

    if (lengthA != 0 && lengthB != 0 && lengthC != 0) {
      int mps = abs(A - lengthA) + (cntA - 1) * 10 +  abs(B - lengthB) + (cntB - 1) * 10 +  abs(C - lengthC) + (cntC - 1) * 10;
      ans = min(mps, ans);
    }
  }
  cout << ans << endl;
}
