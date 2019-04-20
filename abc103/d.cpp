#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

bool
sortByZero(const vector<int> &la, const vector<int> &ra) {return la[0] < ra[0];}

bool
sortByOne(const vector<int> &la, const vector<int> &ra) {return la[1] < ra[1];}

int
main(void) {
  int n, m, i, left, right, counter, _a, _b;

  cin >> n >> m;
  vector< vector<int> > A(m, vector<int>(2));

  for(i=0; i<m; i++) {
    cin >> _a >> _b;
    A[i][0] = _a;
    A[i][1] = _b;
  }
  sort(A.begin(), A.end(), sortByOne);
  sort(A.begin(), A.end(), sortByZero);

  left = -1; right = -1;
  counter = 0;
  for(i=0; i<m; i++) {
    _a = A[i][0];
    _b = A[i][1];
    if (_a < right) {
      left = _a;
      right = min(_b, right);
    } else {
      counter += 1;
      left = _a;
      right = _b;
    }
  }
  cout << counter << endl;

  return 0;
}
