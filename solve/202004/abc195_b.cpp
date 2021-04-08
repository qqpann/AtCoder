#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a, b, w;
    cin >> a >> b >> w;
    w = w * 1000;

    int tms = w / b;
    int sur = w % b; // surplus 剰余
    int mgn = (b - a) * tms + sur;
    // cout << tms << ' ' << sur << ' ' << mgn;
    if (sur != 0 && mgn + sur < a)
    {
        cout << "UNSATISFIABLE" << endl;
    }
    else
    {
        cout << w / b + (w % b ? 1 : 0) << ' ' << w / a << endl;
    }
}