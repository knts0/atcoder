#include<iostream>
#include<utility>
#include<vector>
#include<algorithm>
using namespace std;

bool comp(pair<string, int> a, pair<string, int> b) {
	return a.first < b.first;
}

int main() {
  int n;
  cin >> n;

  string s;
  cin >> s;

  vector<pair<string, int>> substrs[n + 1];  

  // 部分文字列を列挙
  for (int i = 1; i <= n; i++) {
      for (int j = 0; j + (i - 1) < n; j++) {
          substrs[i].push_back(make_pair(s.substr(j, i), j));
      }
  }

  int ans = 0;
  // ソート
  for (int i = 1; i <= n; i++) {
      sort(substrs[i].begin(), substrs[i].end());
      for (int j = 0; j < substrs[i].size(); j++) {
          cout << substrs[i][j].first << " ";
      }
      cout << "" << endl;

      int j = 0;
      int ans = 0;
      while (j < substrs[i].size()) {
        auto itr = upper_bound(substrs[i].begin(), substrs[i].end(), substrs[i][j], comp);
        int k = itr - substrs[i].begin();
        if (k - j > 1 && k < substrs[i].size() - 1 && substrs[i][k - 1].second - substrs[i][j].second >= i) {
          ans = i;
        }
        j = k;
      }
  }

  cout << ans << endl;
}
