#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define REP(i, m, n) for (ll i = (ll)(m); i < (ll)(n); i++)
#define rep(i, n) REP(i, 0, n)

int main()
{
    ll n;
    cin >> n;
    ll ai, ans = 0;
    vector<ll> nl(401); // number line
    rep(i, n)
    {
        cin >> ai;
        ++nl[ai + 200];
    }
    rep(i, 401)
    {
        REP(j, i + 1, 401)
        {
            ll times = nl.at(i) * nl.at(j);
            ans += times * (i - j) * (i - j);
        }
    }
    cout << ans << endl;
}