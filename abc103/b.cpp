#include <iostream>
#include <string>

using namespace std;

int
main(int argc, char* argv[]) {
  string s, t;
  int i, n;
  cin >> s;
  cin >> t;

  n = s.size();
  for(i=0; i<n; i++) {
    if(s == t) {
      cout << "Yes" << endl;
      return 0;
    }
    t = t.substr(1) + t.substr(0,1);
  }
  cout << "No" << endl;
  return 0;
}
