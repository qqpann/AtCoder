#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define REP(i, m, n) for (ll i = (ll)(m); i < (ll)(n); i++)
#define rep(i, n) REP(i, 0, n)

int main()
{
    float r, x, y;
    cin >> r >> x >> y;
    float d = sqrt(x * x + y * y);
    if (d == 0)
    {
        cout << 0 << endl;
    }
    else if (d < r)
    {
        cout << 2 << endl;
    }
    else
    {
        cout << ceil(d / r) << endl;
    }
}