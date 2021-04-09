#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    ll n;
    cin >> n;
    ll ai, ans = 0;
    vector<ll> nl(401); // number line
    for (ll i = 0; i < n; ++i)
    {
        cin >> ai;
        ++nl[ai + 200];
    }
    for (int i = 0; i < 401; ++i)
    {
        for (int j = (i + 1); j < nl.size(); ++j)
        {
            ll times = nl.at(i) * nl.at(j);
            ans += times * (i - j) * (i - j);
        }
    }
    cout << ans << endl;
}