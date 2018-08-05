#include <iostream>
#include <string>
#include <vector>

using namespace std;

int
main(int argc, char* argv[]) {
  int n, _a, i, s;
  vector<int> a;

  cin >> n;

  s = 0;
  for(i=0; i<n; i++) {
    cin >> _a;
    a.push_back(_a);
    s += _a - 1;
  }

  cout << s;

  return 0;
}
