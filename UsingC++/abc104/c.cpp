#include <iostream>
#include <string>
#include <vector>

using namespace std;

int
main(int argc, char* argv[]) {
  int D, G;
  int _p, _c;
  int i, j;
  int tmp, p_size, score;
  vector<int> P, C;
  cin >> D >> G;
  for (i=0; i<D; i++) {
    cin >> _p >> _c;
    P.push_back(_p);
    C.push_back(_c);
  }

  j = 0;
  p_size = P.size();
  for (i=0; i<p_size; i++) {
    score = P.size() - i;
    _p = P.back();
    _c = C.back();
    P.pop_back();
    C.pop_back();
    tmp = G - score * _p - _c;
    if (tmp <= 0) {
      for (i=0; i<_p; i++) {
        j++;
        tmp = G - score;
        if (i == score) {
          tmp -= _c;
        }
        if (tmp < 0) {
          cout << j << endl;
          return 0;
        }
      }
      G = tmp;
    }
    G = tmp;
  }

  return 0;
}
