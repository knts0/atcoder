#include<iostream>
using namespace std;

int main() {
  string S, T;
  cin >> S;
  cin >> T;

  int ans = 0;
  for (int i = 0; i < 3; i++) if (S[i] == T[i]) ans += 1;

  cout << ans << endl;
}
