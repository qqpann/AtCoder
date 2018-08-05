#include <iostream>
#include <string>
#include <vector>

using namespace std;

int
main(int argc, char* argv[]) {
  int n, i;
  long long _a;
  vector<long long> a;

  cin >> n;

  for(i=0; i<n; i++) {
    cin >> _a;
    a.push_back(_a);
  }
  sort(a.begin(), a.end());

  long long int b = (a.back() - *a.begin());
  cout << b << endl;

  return 0;
}
