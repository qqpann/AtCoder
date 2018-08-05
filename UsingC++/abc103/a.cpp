#include <iostream>
#include <string>
#include <vector>

using namespace std;

int
main(int argc, char* argv[]) {
  int _a, i;
  vector<int> A;

  for(i=0; i<3; i++) {
    cin >> _a;
    A.push_back(_a);
  }
  sort(A.begin(), A.end());

  cout << A.back() - *A.begin() << endl;

  return 0;
}
