#include <iostream>
#include <string>

using namespace std;

int
main(int argc, char* argv[]) {
  int n;

  cin >> n;

  if (n % 2 == 0) {
    cout << n << endl;
  } else {
    cout << n * 2 << endl;
  }

  return 0;
}
