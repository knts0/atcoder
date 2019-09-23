#include<iostream>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  int current = 1;
  int ans = 0;
  while (current >= b) {
    current += a;
    current -= 1;
  }
  cout << ans << endl;
}
